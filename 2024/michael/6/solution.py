import sys
import copy

with open('C:/Users/Michael/workspace/aoc_23/2024/michael/6/input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

dirMap = {
    '^': (-1, 0, '>'),
    '>': (0, 1, 'v'),
    'v': (1, 0, '<'),
    '<': (0, -1, '^')
}
d = ''
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            d = '^'
            break
    if d:
        break

## P1
def P1(grid, i, j, d):
    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
        di, dj, dd = dirMap[d]
        # Obstacle
        try:
            if grid[i+di][j+dj] == '#':
                d = dd
                continue
        except IndexError:
            grid[i][j] = 'X'
            break
        # Clear path
        grid[i][j] = 'X'
        i += di
        j += dj
        # for g in grid:
        #     print(''.join(g))
        # print('----------------')

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                total += 1

    return total

## P2 - brute force!
def P2(grid, i, j, d):
    startI, startJ, startD = i, j, d
    startGrid = copy.deepcopy(grid)

    # Convert grid elements to sets
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] = {grid[x][y]} 

    total = 0
    for x in range(len(grid)):
        print(x)
        for y in range(len(grid[0])):
            if grid[x][y] == {'^'} or grid[x][y] == {'#'}:
                continue
            tempGrid = copy.deepcopy(grid)
            tempGrid[x][y] = {'#'}
            if checkLoop(tempGrid, i, j, d):
                total += 1

    return total

def checkLoop(grid, i, j, d):
    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
        di, dj, dd = dirMap[d]
        # Check if we've already been here in this direction
        if d in grid[i][j] and '.' in grid[i][j]:
            return True

        # Step
        # Obstacle
        try:
            if grid[i+di][j+dj] == {'#'}:
                d = dd
                continue
        except IndexError:
            break
        # Clear path
        grid[i][j].add(d)
        i += di
        j += dj
    return False

print(P2(grid, i, j, d))