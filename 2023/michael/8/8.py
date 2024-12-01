import sys, math

# P1
def loadInput(fname):
    # Return (LR, {aaa: (bbb, ccc)})
    with open(fname, 'r') as f:
        lines = f.readlines()
    lr = lines[0].strip()

    m = {}
    for line in lines[2:]:
        x = line.split()[0]
        (a, b) = line.split('(')[1].split(', ')
        b = b[:3]
        m[x] = (a, b)
    return (lr, m)


'''if __name__ == '__main__':
    (lr, maps) = loadInput(sys.argv[1])
    step = 'AAA'
    count = 0
    index = 0
    while step != 'ZZZ':
        side = lr[index]
        if side == 'L':
            step = maps[step][0]
        else:
            step = maps[step][1]
        count += 1
        index = (index + 1) % len(lr)
    print(count)'''

# P2
def cycleLength(startStep, lr, maps):
    # (stepsToCycle, cycleLen, zsFromStartCycle)
    step = startStep
    index = 0
    count = 0
    seenWhen = {}
    zsFromStart = []
    while (step, index) not in seenWhen:
        seenWhen[(step, index)] = count
        side = lr[index]
        if side == 'L':
            step = maps[step][0]
        else:
            step = maps[step][1]
        count += 1
        index = (index + 1) % len(lr)
        if step[-1] == 'Z':
            zsFromStart += [count]
    zsFromStart = filter(lambda x: x > seenWhen[(step, index)], zsFromStart)
    zsFromStart = [x-seenWhen[(step, index)] for x in zsFromStart]
    return (seenWhen[(step, index)], 
            count - seenWhen[(step, index)],
            zsFromStart)

if __name__ == '__main__':
    (lr, maps) = loadInput(sys.argv[1])
    startSteps = [x for x in maps if x[-1] == 'A']
    cycleLens = []
    for x in startSteps:
        print(x)
        (stepsToCycle, cycleLen, zsFromStartCycle) = cycleLength(x, lr, maps)
        # print(stepsToCycle)
        # print(zsFromStartCycle)
        # Conveniently, all entry points into the cycles are equidistant to the distance from Z to cycle start,
        #   (i.e. stepsToCycle + zsFromStartCycle == cycleLen), and there's only one Z in each cycle,
        #   so we can just take LCM of all cycle lengths. This definitely isn't guaranteed, but they set up the
        #   data this way.
        print(cycleLen)
        cycleLens += [cycleLen]
    print(math.lcm(*cycleLens))
    