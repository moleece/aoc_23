import sys

# P1 - nothing clever
def findReflection(lines):
    candidates = set(range(1, len(lines[0])))
    for line in lines:
        candidates = set(filter(lambda x: isReflection(line, x), candidates))
        if len(candidates) == 0:
            return -1
    return list(candidates)[0]

def isReflection(line, x):
    # Check if x is reflection point for line
    i = 1
    while x-i >= 0 and x+i-1 < len(line):
        if line[x-i] != line[x+i-1]:
            return False
        i += 1
    return True

# P2 - maybe clever? Worked first try with no debugging at least :)
def findSmudgeReflection(lines):
    candidates =  range(1, len(lines[0]))
    for c in candidates:
        m = buildReflectionMatrix(lines, c)
        onesCount = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 1:
                    onesCount += 1
        if onesCount == 1:
            return c
    return -1

def buildReflectionMatrix(lines, c):
    w = min(c, len(lines[0]) - c)
    m = [[0]*w for _ in range(len(lines))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if lines[i][c+j] == '#':
                m[i][j] += 1
            if lines[i][c-j-1] == '#':
                m[i][j] += 1
    return m

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        text = f.read()
    blocks = text.split('\n\n')
    blocks = [x.split('\n') for x in blocks]

    total = 0
    for b in blocks:
        x = findSmudgeReflection(b)
        if x != -1:
            total += x
        else:
            transpose = [''.join(s) for s in zip(*b)]
            x = findSmudgeReflection(transpose)
            if x == -1:
                print()
                for l in transpose:
                    print(l)
            total += 100*x
    print(total)
    