import sys

# P1
def HASH(h):
    val = 0
    for c in h:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

# P2
def doSteps(steps):
    boxes = {i:[] for i in range(256)}
    for step in steps:
        label = step.split('-')[0].split('=')[0]
        h = HASH(label)
        if '-' in step:
            boxes[h] = list(filter(lambda x: x[0] != label, boxes[h]))
        else: # '='
            lens = int(step[-1])
            newBox = []
            replaced = False
            for l in boxes[h]:
                if l[0] == label:
                    newBox += [(label, lens)]
                    replaced = True
                else:
                    newBox += [l]
            if not replaced:
                newBox += [(label, lens)]
            boxes[h] = newBox
    return boxes
        

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        line = f.readline().strip()
    total = 0
    # for h in line.split(','):
    #     total += HASH(h)
    boxes = doSteps(line.split(','))
    for i in boxes:
        for j in range(len(boxes[i])):
            (label, lens) = boxes[i][j]
            total += (i+1) * (j+1) * lens
    print(total)