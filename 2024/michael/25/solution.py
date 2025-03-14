import sys

def readKey(lines):
    key = []
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[len(lines)-1-j][i] != '#':
                key.append(j-1)
                break
    return tuple(key)

def readLock(lines):
    lock = []
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[j][i] != '#':
                lock.append(j-1)
                break
    return tuple(lock)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]

    keys = []
    locks = []
    i = 0
    while i < len(lines):
        if lines[i][0] == '.':
            keys += [readKey(lines[i:i+7])]
        else:
            locks += [readLock(lines[i:i+7])]
        i += 8
    
    # print("Keys:")
    # for k in keys:
    #     print(k)
    # print("Locks:")
    # for l in locks:
    #     print(l)

    fitCount = 0
    for k in keys:
        for l in locks:
            fit = True
            for i in range(len(k)):
                if k[i] + l[i] > 5:
                    fit = False
                    break
            if fit:
                fitCount += 1
    print(fitCount)
