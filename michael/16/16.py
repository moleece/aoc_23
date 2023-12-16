import sys

# P1
class Cell:

    def __init__(self, char):
        self.char = char
        self.lightDirs = set()
    
    def receiveLightFromDir(self, dir):
        # Returns output dirs
        newDirs = set(dirCharMap[self.char][dir]).difference(self.lightDirs)
        self.lightDirs = self.lightDirs.union(newDirs)
        return list(newDirs)


def makeGrid(lines):
    grid = []
    for i in range(len(lines)):
        gridLine = []
        for j in range(len(lines[i])):
            gridLine += [Cell(lines[i][j])]
        grid += [gridLine]
    return grid

def visGrid(grid):
    s = ''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = grid[i][j]
            if c.char != '.' or len(c.lightDirs) == 0:
                s += c.char
            elif len(c.lightDirs) > 1:
                s += str(len(c.lightDirs))
            else:
                s += list(c.lightDirs)[0]
        s += '\n'
    print(s)




dirCharMap = {
    '.': {'s': ['s'], 'n': ['n'], 'e':['e'], 'w':['w']},
    '\\': {'s': ['e'], 'n': ['w'], 'e':['s'], 'w':['n']},
    '/': {'s': ['w'], 'n': ['e'], 'e':['n'], 'w':['s']},
    '|': {'s': ['s'], 'n': ['n'], 'e':['n', 's'], 'w':['n', 's']},
    '-': {'s': ['e', 'w'], 'n': ['e', 'w'], 'e':['e'], 'w':['w']}
}

dirPosChange = {'n':(-1,0),
          's':(1,0),
          'w':(0,-1),
          'e':(0,1)}

# P2
def energizeCount(i, j, dir, lines):
    grid = makeGrid(lines)

    stepsToTake = [(i,j,dir)]

    while len(stepsToTake) > 0:
        # visGrid(grid)
        # print()
        (i, j, dir) = stepsToTake.pop()
        newDirs = grid[i][j].receiveLightFromDir(dir)
        for d in newDirs:
            (di, dj) = dirPosChange[d]
            if i+di >= len(grid) or i+di < 0 or j + dj >= len(grid[0]) or j + dj < 0:
                continue
            stepsToTake += [(i+di, j+dj, d)]
    
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if len(grid[i][j].lightDirs) > 0:
                total += 1
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    
    best = 0
    for i in range(len(lines)):
        best = max(best, energizeCount(i, 0, 'e', lines))
        best = max(best, energizeCount(i, len(lines[0])-1, 'w', lines))
    for j in range(len(lines[0])):
        best = max(best, energizeCount(len(lines)-1, j, 'n', lines))
        best = max(best, energizeCount(0, j , 's', lines))
    print(best)
    