import sys
from collections import defaultdict


def is_valid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def next_steps(grid, currentLocations, targetHeight):
    newLocations = set()
    for i, j in currentLocations:
        for i2, j2 in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if is_valid(grid, i2, j2) and grid[i2][j2] == targetHeight:
                newLocations.add((i2, j2))
    return newLocations

### P1
def score_trailhead(grid, i, j):
    if grid[i][j] != 0:
        return 0
    
    targetHeight = 1
    currentLocations = {(i, j)}
    while targetHeight < 10:
        currentLocations = next_steps(grid, currentLocations, targetHeight)
        targetHeight += 1

    return len(currentLocations)


def next_steps_rating(grid, currentLocations, targetHeight):
    newLocations = defaultdict(int)
    for i, j in currentLocations:
        for i2, j2 in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if is_valid(grid, i2, j2) and grid[i2][j2] == targetHeight:
                newLocations[(i2, j2)] += currentLocations[(i, j)]
    return newLocations



### P2
def score_trailhead_rating(grid, i, j):
    if grid[i][j] != 0:
        return 0

    targetHeight = 1
    currentLocations = {(i, j):1}
    while targetHeight < 10:
        currentLocations = next_steps_rating(grid, currentLocations, targetHeight)
        targetHeight += 1

    return sum(currentLocations.values())


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        grid = [list(map(int, list(line.strip()))) for line in f.readlines()]
    
    # P1
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += score_trailhead(grid, i, j)
    print(total)

    # P2
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += score_trailhead_rating(grid, i, j)
    print(total)
