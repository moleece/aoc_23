import sys


def move_p1(grid, dir, roboI, roboJ):
    blocksToMove = 0
    newI, newJ = roboI, roboJ
    if dir == '<':
        ti, tj = roboI, roboJ - 1
        while True:
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                grid[roboI][roboJ] = '.'
                grid[roboI][roboJ-1] = '@'
                newI, newJ = roboI, roboJ - 1
                for i in range(blocksToMove):
                    grid[roboI][roboJ - i - 2] = 'O'
                break
            blocksToMove += 1
            tj -= 1
    elif dir == '>':
        ti, tj = roboI, roboJ + 1
        while True:
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                grid[roboI][roboJ] = '.'
                grid[roboI][roboJ+1] = '@'
                newI, newJ = roboI, roboJ + 1
                for i in range(blocksToMove):
                    grid[roboI][roboJ + i + 2] = 'O'
                break
            blocksToMove += 1
            tj += 1
    elif dir == '^':
        ti, tj = roboI - 1, roboJ
        while True:
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                grid[roboI][roboJ] = '.'
                grid[roboI-1][roboJ] = '@'
                newI, newJ = roboI - 1, roboJ
                for i in range(blocksToMove):
                    grid[roboI - i - 2][roboJ] = 'O'
                break
            blocksToMove += 1
            ti -= 1
    elif dir == 'v':
        ti, tj = roboI + 1, roboJ
        while True:
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                grid[roboI][roboJ] = '.'
                grid[roboI+1][roboJ] = '@'
                newI, newJ = roboI + 1, roboJ
                for i in range(blocksToMove):
                    grid[roboI + i + 2][roboJ] = 'O'
                break
            blocksToMove += 1
            ti += 1
    return grid, newI, newJ


def move_p2(grid, dir, roboI, roboJ):
    newI, newJ = roboI, roboJ
    if dir == '<':
        blocksToMove = 0
        ti, tj = roboI, roboJ - 1
        while True:
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                grid[roboI][roboJ] = '.'
                grid[roboI][roboJ-1] = '@'
                newI, newJ = roboI, roboJ - 1
                for i in range(blocksToMove):
                    grid[roboI][roboJ - 2*i - 3] = '['
                    grid[roboI][roboJ - 2*i - 2] = ']'
                break
            blocksToMove += 1
            tj -= 2
        return grid, newI, newJ
    elif dir == '>':
        blocksToMove = 0
        ti, tj = roboI, roboJ + 1
        while True:
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                grid[roboI][roboJ] = '.'
                grid[roboI][roboJ+1] = '@'
                newI, newJ = roboI, roboJ + 1
                for i in range(blocksToMove):
                    grid[roboI][roboJ + 2*i + 3] = ']'
                    grid[roboI][roboJ + 2*i + 2] = '['
                break
            blocksToMove += 1
            tj += 2
        return grid, newI, newJ
    elif dir == '^':
        squaresToCheck = [(roboI-1, roboJ)]
        squaresToMoveUp = [(roboI, roboJ)]
        while squaresToCheck:
            ti, tj = squaresToCheck.pop()
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                continue
            elif grid[ti][tj] == ']':
                squaresToCheck += [(ti-1, tj), (ti-1, tj-1)]
                squaresToMoveUp += [(ti, tj), (ti, tj-1)]
            elif grid[ti][tj] == '[':
                squaresToCheck += [(ti-1, tj), (ti-1, tj+1)]
                squaresToMoveUp += [(ti, tj), (ti, tj+1)]
        squaresToMoveUp = sorted(list(set(squaresToMoveUp)), key=lambda x: x[0])
        for i, j in squaresToMoveUp:
            grid[i-1][j] = grid[i][j]
            grid[i][j] = '.'
        return grid, roboI - 1, roboJ
    elif dir == 'v':
        squaresToCheck = [(roboI+1, roboJ)]
        squaresToMoveDown = [(roboI, roboJ)]
        while squaresToCheck:
            ti, tj = squaresToCheck.pop()
            if grid[ti][tj] == '#':
                return grid, roboI, roboJ
            elif grid[ti][tj] == '.':
                continue
            elif grid[ti][tj] == ']':
                squaresToCheck += [(ti+1, tj), (ti+1, tj-1)]
                squaresToMoveDown += [(ti, tj), (ti, tj-1)]
            elif grid[ti][tj] == '[':
                squaresToCheck += [(ti+1, tj), (ti+1, tj+1)]
                squaresToMoveDown += [(ti, tj), (ti, tj+1)]
        squaresToMoveDown = sorted(list(set(squaresToMoveDown)), key=lambda x: x[0], reverse=True)
        for i, j in squaresToMoveDown:
            grid[i+1][j] = grid[i][j]
            grid[i][j] = '.'
        return grid, roboI + 1, roboJ




def display_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def broken_grid(grid, new_grid):
    newCount = oldCount = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == '[' and new_grid[i][j+1] != ']':
                print("Mismatch")
                return True
            if new_grid[i][j] == '[':
                newCount += 1
            if grid[i][j] == '[':
                oldCount += 1
    if newCount != oldCount:
        print(newCount, oldCount)
    return newCount != oldCount

def grid_cost(grid):
    cost = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                cost += i*100 + j
    return cost

def grid_cost_p2(grid):
    cost =0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '[':
                cost += i*100 + j
    return cost

if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], 'r') as f:
        line = f.readline().strip()
        while line:
            grid.append(list(line))
            line = f.readline().strip()
        
        instrs = f.read().replace('\n', '') 
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                roboI, roboJ = i, j

    for i in instrs:
        grid, roboI, roboJ = move_p1(grid, i, roboI, roboJ)
        # print(i)
        # display_grid(grid)
    
    print(grid_cost(grid))

    # P2
    grid = []
    with open(sys.argv[1], 'r') as f:
        line = f.readline().strip()
        while line:
            grid.append(list(line.replace('.', '..').replace('@', '@.').replace('O', '[]').replace('#', '##')))
            line = f.readline().strip()
        
        instrs = f.read().replace('\n', '') 

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                roboI, roboJ = i, j
    
    blockCount = sum([row.count('[') for row in grid])
    print(blockCount)

    c = 0
    for i in instrs:
        c += 1
        new_grid, roboI, roboJ = move_p2(grid, i, roboI, roboJ)
        # if c < 24 and c > 18:
        #     print(c)
        #     print(i)
        #     display_grid(new_grid)
        grid = new_grid

    display_grid(grid)
    print(grid_cost_p2(grid))



        