import sys
from collections import defaultdict

def get_cheats(grid, path, cheat_length=2):
    cheats = defaultdict(int)
    for (i,j) in path:
        for di in range(-1*cheat_length, cheat_length+1):
            for dj in range(-1*cheat_length, cheat_length+1):
                if abs(di) + abs(dj) > cheat_length:
                    continue
                if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j+dj >= len(grid[0]):
                    continue
                if grid[i+di][j+dj] != '#' and grid[i+di][j+dj] - grid[i][j] > abs(di) + abs(dj):
                    cheats[grid[i+di][j+dj] - grid[i][j] - abs(di) - abs(dj)] += 1
    return cheats




if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        grid = [list(line.strip()) for line in f]
    
    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)
    
    p = 0
    path = []
    while start != end:
        i, j = start
        grid[i][j] = p
        path += [(i, j)]
        if str(grid[i-1][j]) in '.E':
            start = (i-1, j)
        elif str(grid[i+1][j]) in '.E':
            start = (i+1, j)
        elif str(grid[i][j-1]) in '.E':
            start = (i, j-1)
        elif str(grid[i][j+1]) in '.E':
            start = (i, j+1)
        p += 1

    grid[end[0]][end[1]] = p

    #P1 
    cheats = get_cheats(grid, path, 2)
    print(sum([cheats[c] for c in cheats if c >= 100]))

    # P2
    cheats = get_cheats(grid, path, 20)
    print(sum([cheats[c] for c in cheats if c >= 100]))