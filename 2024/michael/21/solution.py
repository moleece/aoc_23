import sys, itertools

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

    
def numsToArrows(numString):
    numPos = {
        '7': (0,0),
        '8': (0,1),
        '9': (0,2),
        '4': (1,0),
        '5': (1,1),
        '6': (1,2),
        '1': (2,0),
        '2': (2,1),
        '3': (2,2),
        '0': (3,1),
        'A': (3,2)
    }

    pos = (3,2)
    seq = ''
    for num in numString:
        newPos = numPos[num]
        dy = newPos[0] - pos[0]
        dx = newPos[1] - pos[1]
        toAdd = []
        if pos[0] == 3 and newPos[1] == 0:
            sortOrder = '^v<>'
        else:
            sortOrder = '<>^v'
        if dx > 0:
            toAdd += ['>'] * dx
        else:
            toAdd += ['<'] * -dx
        if dy > 0:
            toAdd += ['v'] * dy
        else:
            toAdd += ['^'] * -dy
        toAdd = sorted(toAdd, key=lambda x: sortOrder.index(x))
        seq += ''.join(toAdd)
        seq += 'A'
        pos = newPos
    return seq

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

def arrowsToArrows(arrowString):
    arrowPos = {
        '^': (0,1),
        'A': (0,2),
        '<': (1,0),
        'v': (1,1),
        '>': (1,2)
    }
    pos = (0,2)
    seq = ''
    for arrow in arrowString:
        newPos = arrowPos[arrow]
        dy = newPos[0] - pos[0]
        dx = newPos[1] - pos[1]
        toAdd = []
        if pos[0] == 0 and newPos[1] == 0:
            sortOrder = '^v<>'
        else:
            sortOrder = '<>^v'
        if dx > 0:
            toAdd += ['>'] * dx
        else:
            toAdd += ['<'] * -dx
        if dy > 0:
            toAdd += ['v'] * dy
        else:
            toAdd += ['^'] * -dy
        toAdd = sorted(toAdd, key=lambda x: sortOrder.index(x))
        seq += ''.join(toAdd)
        seq += 'A'
        pos = newPos
    return seq


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]
    
    total = 0
    for numLine in lines:
        instrLen = len(arrowsToArrows(arrowsToArrows(numsToArrows(numLine))))
        code = int(numLine[:-1])
        print(numsToArrows(numLine))
        print(arrowsToArrows(numsToArrows(numLine)))
        print(numLine, '-', instrLen)
        total += instrLen * code
    print(total)