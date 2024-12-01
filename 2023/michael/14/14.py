import sys

# P1 inefficient
def rollNorth(lines):
    for i in range(len(lines)-1, 0, -1):
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                if lines[i-1][j] != '.':
                    continue
                lines[i-1][j] = 'O'
                k = i+1
                while k < len(lines):
                    if lines[k][j] != 'O':
                        break
                    k += 1
                lines[k-1][j] = '.'
    return lines

# P2
def rollSouth(lines):
    for i in range(len(lines)-1):
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                if lines[i+1][j] != '.':
                    continue
                lines[i+1][j] = 'O'
                k = i-1
                while k >= 0:
                    if lines[k][j] != 'O':
                        break
                    k -= 1
                lines[k+1][j] = '.'
    return lines

def rollEast(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])-1):
            if lines[i][j] == 'O':
                if lines[i][j+1] != '.':
                    continue
                lines[i][j+1] = 'O'
                k = j-1
                while k >= 0:
                    if lines[i][k] != 'O':
                        break
                    k -= 1
                lines[i][k+1] = '.'
    return lines

def rollWest(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])-1, 0, -1):
            if lines[i][j] == 'O':
                if lines[i][j-1] != '.':
                    continue
                lines[i][j-1] = 'O'
                k = j+1
                while k < len(lines[0]):
                    if lines[i][k] != 'O':
                        break
                    k += 1
                lines[i][k-1] = '.'
    return lines

def lineHash(lines, dir):
    return hash(''.join([''.join(l) for l in lines]) + dir)



def totalLoad(lines):
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                total += len(lines) - i
    return total


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    
    dirs = [('n', rollNorth), ('w',rollWest), ('s', rollSouth), ('e',rollEast)]
    hashes = {}
    i = 0

    while lineHash(lines, dirs[i%4][0]) not in hashes:
        hashes[lineHash(lines, dirs[i%4][0])] = i
        lines = dirs[i%4][1](lines)
        i += 1
    cycleLen = i - hashes[lineHash(lines, dirs[i%4][0])]
    
    print(i, cycleLen)

    numTilts = int((4000000000 - i) / cycleLen)
    i += cycleLen * numTilts
    while i < 4000000000:
        lines = dirs[i%4][1](lines)
        i += 1
    print(totalLoad(lines))