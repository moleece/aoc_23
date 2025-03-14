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



## Take 2, search
def numberPadOptions(numString):
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
    seqs = ['']
    for num in numString:
        newPos = numPos[num]
        dy = newPos[0] - pos[0]
        dx = newPos[1] - pos[1]
        path1 = ('v' if dy > 0 else '^') * abs(dy) + ('>' if dx > 0 else '<') * abs(dx) + 'A'
        path2 = ('>' if dx > 0 else '<') * abs(dx) + ('v' if dy > 0 else '^') * abs(dy) + 'A'
        if pos[0] == 3 and newPos[1] == 0:
            newPaths = [path1]
        elif pos[1] == 0 and newPos[0] == 3:
            newPaths = [path2]
        else:
            newPaths = [path1, path2]

        newSeqs = []
        for s in seqs:
            for p in newPaths:
                newSeqs.append(s + p)
        seqs = newSeqs
        pos = newPos
    return list(set(seqs))

def arrowPadOptions(arrowString):
    arrowPos = {
        '^': (0,1),
        'A': (0,2),
        '<': (1,0),
        'v': (1,1),
        '>': (1,2)
    }
    pos = (0,2)
    seqs = ['']
    for arrow in arrowString:
        newPos = arrowPos[arrow]
        dy = newPos[0] - pos[0]
        dx = newPos[1] - pos[1]
        path1 = ('v' if dy > 0 else '^') * abs(dy) + ('>' if dx > 0 else '<') * abs(dx) + 'A'
        path2 = ('>' if dx > 0 else '<') * abs(dx) + ('v' if dy > 0 else '^') * abs(dy) + 'A'
        if pos[0] == 0 and newPos[1] == 0:
            newPaths = [path1]
        elif pos[1] == 0 and newPos[0] == 0:
            newPaths = [path2]
        else:
            newPaths = [path1, path2]

        newSeqs = []
        for s in seqs:
            for p in newPaths:
                newSeqs.append(s + p)
        seqs = newSeqs
        pos = newPos
    return list(set(seqs))

# Take 3, efficient?
def numberPadOpt(numString):
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
        path1 = ('v' if dy > 0 else '^') * abs(dy) + ('>' if dx > 0 else '<') * abs(dx) + 'A'
        path2 = ('>' if dx > 0 else '<') * abs(dx) + ('v' if dy > 0 else '^') * abs(dy) + 'A'
        if pos[0] == 3 and newPos[1] == 0:
            seq += path1
        elif pos[1] == 0 and newPos[0] == 3:
            seq += path2
        else:
            if path2 == '>vA':
                path2 = 'v>A'
            elif path2 == '<^A':
                path2 = '^<A'
            elif path2 == '>vvvA':
                path2 = 'vvv>A'
            seq += path2
        pos = newPos
    return seq

def arrowPadOpt(arrowString):
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
        path1 = ('v' if dy > 0 else '^') * abs(dy) + ('>' if dx > 0 else '<') * abs(dx) + 'A'
        path2 = ('>' if dx > 0 else '<') * abs(dx) + ('v' if dy > 0 else '^') * abs(dy) + 'A'
        if pos[0] == 0 and newPos[1] == 0:
            seq += path1
        elif pos[1] == 0 and newPos[0] == 0:
            seq += path2
        else:
            seq += path2
        pos = newPos

    return seq


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]
    
    # total = 0
    # for numLine in lines[1:2]:
    #     print(numLine)
    #     shortestArrow = 10000000
    #     opts = numberPadOptions(numLine)
    #     for opt in opts:
    #         arrows1 = arrowPadOptions(opt)
    #         i = 0
    #         for arrow1 in arrows1:
    #             i += 1
    #             # print(i, '/', len(arrows1))
    #             arrows2 = arrowPadOptions(arrow1)
    #             bestPath = min([len(x) for x in arrows2])
    #             if bestPath < shortestArrow:
    #                 shortestArrow = bestPath
    #                 best1 = arrow1
    #                 best2 = [x for x in arrows2 if len(x) == bestPath][0]
    #                 best0 = opt
    #     print(shortestArrow)
    #     print(best0)
    #     print(best1)
    #     print(best2)
    #     total += int(numLine[:-1]) * shortestArrow
    #     print()

    #     # 803A - 
    #     # 528A
    #     # 586A
    #     # 341A
    #     # 319A
    
    # print(total)

    total = 0
    for numLine in lines:
        # instrLen = len(arrowPadOpt(arrowPadOpt(numberPadOpt(numLine))))
        code = int(numLine[:-1])
        # print(numLine, '-', instrLen)
        print(numberPadOpt(numLine))
        # print(arrowPadOpt(numberPadOpt(numLine)))
        # print(arrowPadOpt(arrowPadOpt(numberPadOpt(numLine))))
        # total += instrLen * code
    print(total)

    # total = 0
    # for numLine in lines:
    #     arrows = numberPadOpt(numLine)
    #     for i in range(25):
    #         print(i)
    #         print(len(arrows))
    #         arrows = arrowPadOpt(arrows)
    #     instrLen = len(arrows)
    #     code = int(numLine[:-1])
    #     print(numLine, '-', instrLen)
    #     print(len(arrows))
    #     total += instrLen * code
    # print(total)



# OPT(c1, c2, k) = number of moves to get from c1 to c2 and press c2 with k levels of indirection
# OPT(c1, c2, k) = OPT(A, leftarrow, k-1) + (num left presses-1) + OPT(leftarrow, uparrow, k-1) + (num up presses-1)
#                     + OPT(uparrow, A, k-1) + 1

