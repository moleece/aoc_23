import sys
import functools

# P1
def numOptionsRoot(line):
    # Parse
    (states, seq) = line.split()
    seq = tuple(map(int, seq.split(',')))

    # Part 2 - Unfold
    states = '?'.join([states] * 5)
    seq = seq * 5

    # DP
    # opt[i][j] = # options starting block i in sequence at position j in state
    global opt 
    opt = [[None] * len(states) for i in range(len(seq))]
    n = 0
    for i in range(len(states)):
        newN = numOptions(i, 0, states, seq)
        n = n + newN
        if states[i] == '#':
            break
    # for o in opt:
    #     print(o)
    # print(n)
    return n

nOptionCalls = {'x': 0}
nCached = {'x': 0}

@functools.cache
def numOptions(stateStart, seqStart, states, seq):
    global opt
    # nOptionCalls['x'] += 1
    # if nOptionCalls['x'] % 100000 == 0:
    #     print("nOptionCalls", nOptionCalls['x'])

    if seqStart >= len(opt) and stateStart >= len(opt[0]):
        # nCached['x'] += 1
        # if nCached['x'] % 100000 == 0:
        #     print("nCached", nCached['x'])
        return 1
    
    if seqStart >= len(opt) or stateStart >= len(opt[0]):
        # nCached['x'] += 1
        # if nCached['x'] % 100000 == 0:
        #     print("nCached", nCached['x'])
        return 0

    if opt[seqStart][stateStart]:
        # nCached['x'] += 1
        # if nCached['x'] % 100000 == 0:
        #     print("nCached", nCached['x'])
        return opt[seqStart][stateStart]
    
    for i in range(stateStart, stateStart + seq[seqStart]):
        if i >= len(states) or (states[i] != '#' and states[i] != '?'):
            opt[seqStart][stateStart] = 0
            return 0

    if stateStart + seq[seqStart] < len(states) and states[stateStart + seq[seqStart]] == '#':
        opt[seqStart][stateStart] = 0
        return 0
    
    # Check if we have unaccounted for #s if we should be done
    if seqStart == len(seq) - 1:
        for i in range(stateStart + seq[seqStart] + 1, len(states)):
            if states[i] == '#':
                opt[seqStart][stateStart] = 0
                return 0
    
    newBlockStart = stateStart + seq[seqStart] + 1
    n = numOptions(newBlockStart, seqStart + 1, states, seq)
    if newBlockStart < len(states) and states[newBlockStart] != '#':
        for nextStart in range(newBlockStart + 1, len(states)+1):
            newN = numOptions(nextStart, seqStart + 1, states, seq)
            n = n + newN
            if nextStart < len(states) and states[nextStart] == '#':
                break
            
    opt[seqStart][stateStart] = n
    return n

if __name__ == '__main__':
    # with open('michael/12/ex_clean') as f:
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    count = 0
    for i in range(len(lines)):
        if i % 10 == 0:
            print(i)
        line = lines[i]
        count += numOptionsRoot(line)
    print(count)