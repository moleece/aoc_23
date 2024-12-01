import sys

def getDigstructions(lines):
    digs = []
    for line in lines:
        s = line.split()
        digs += [(s[0], int(s[1]))]
    return digs

dirPosChange = {'U':(-1,0),
          'D':(1,0),
          'L':(0,-1),
          'R':(0,1)}

rightMap = {'U': 'R', 'D': 'L', 'R': 'D', 'L':'U'}
leftMap = {'U': 'L', 'D': 'R', 'R': 'U', 'L':'D'}

def digGrid(digs):
    i, j = 0,0
    cells = []
    rightCells = []
    leftCells = []
    for (d, v) in digs:
        (di, dj) = dirPosChange[d]
        (rdi, rdj) = dirPosChange[rightMap[d]]
        (ldi, ldj) = dirPosChange[leftMap[d]]
        for k in range(v):
            cells += [(i+di*k, j+dj*k)]
            rightCells += [(i+di*k+rdi, j+dj*k+rdj)]
            leftCells += [(i+di*k+ldi, j+dj*k+ldj)]
        i, j = i+di*v, j + dj*v

    minI = min([x[0] for x in cells])
    minJ = min([x[1] for x in cells])
    cells = [(c[0]-minI, c[1]-minJ) for c in cells]
    rightCells = [(c[0]-minI, c[1]-minJ) for c in rightCells]
    leftCells = [(c[0]-minI, c[1]-minJ) for c in leftCells]

    h, w = max([x[0] for x in cells])+1, max([x[1] for x in cells])+1
    grid = [['.']*w for _ in range(h)]
    
    for i,j in cells:
        grid[i][j] = '#'
    for i in range(len(rightCells)):
        (ri, rj) = rightCells[i]
        if ri < 0 or ri >= len(grid) or rj < 0 or rj >= len(grid[0]):
            continue
        if grid[ri][rj] == '.':
            grid[ri][rj] = 'r'
    for i in range(len(leftCells)):
        (li, lj) = leftCells[i]
        if li < 0 or li >= len(grid) or lj < 0 or lj >= len(grid[0]):
            continue
        if grid[li][lj] == '.':
            grid[li][lj] = 'l'
    
    # Flood fill
    changed = True
    while changed:
        changed = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '.':
                    for d in dirPosChange:
                        (di, dj) = dirPosChange[d]
                        if i + di >= len(grid) or j + dj >= len(grid[0]) or i + di < 0 or j + dj < 0:
                            continue
                        if grid[i+di][j+dj] == 'r':
                            changed = True
                            grid[i][j] = 'r'
                        elif grid[i+di][j+dj] == 'l':
                            changed = True
                            grid[i][j] = 'l'
    
    # Find a l or r on border
    innerSide = ''
    for i in range(len(grid)):
        if grid[i][0] == 'l' or grid[i][-1] == 'l':
            innerSide = 'r'
            break
        if grid[i][0] == 'r' or grid[i][-1] == 'r':
            innerSide = 'l'
            break
    for i in range(len(grid[0])):
        if grid[0][i] == 'l' or grid[-1][i] == 'l':
            innerSide = 'r'
            break
        if grid[0][i] == 'r' or grid[-1][i] == 'r':
            innerSide = 'l'
            break

    return sum([l.count('#') for l in grid]) + sum([l.count(innerSide) for l in grid])
    


# P2 - Fine, we'll look something up
def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def area2(p):
    area = 0
    n = len(p)
    p += [(0,0)]
    for i in range(0, n, 2):
        area += p[i+1][0]*(p[i+2][1]-p[i][1]) + p[i+1][1]*(p[i][0]-p[i+2][0])
    return area / 2

def segments(p):
    return zip(p, p[1:] + [p[0]])

def getPointList(lines):
    hexes = [line.split()[-1].strip()[1:-1] for line in lines]
    dirs = ['R', 'D', 'L', 'U']
    instrs = []
    for h in hexes:
        d = dirs[int(h[-1])]
        v = int(h.replace('#', '0x')[:-1], 16)
        instrs += [(d,v)]
        
    # Step through
    x, y = 0, 0
    points = []
    for (d, v) in instrs:
        (di, dj) = dirPosChange[d]
        x,y = x+v*dj, y+v*di
        points += [(x,y)]
    
    return area(points) + sum([x[1] for x in instrs])/2 + 1 # Add the trench itself, since polygon computation is borderless



if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    digs = getPointList(lines)
    #total = digGrid(digs)
    print(digs)