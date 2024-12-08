import sys
from collections import defaultdict

with open(sys.argv[1], 'r') as f:
    grid = [line.strip() for line in f.readlines()]

locations = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            locations[grid[i][j]].append((i, j))


def is_valid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

## P1
def count_antinodes():
    antinodes = set()
    for k in locations:
        for x in range(len(locations[k])-1):
            for y in range(x+1, len(locations[k])):
                (i1, j1), (i2, j2) = locations[k][x], locations[k][y]
                di, dj = i2-i1, j2-j1
                if is_valid(i1-di, j1-dj):
                    antinodes.add((i1-di, j1-dj))
                if is_valid(i2+di, j2+dj):
                    antinodes.add((i2+di, j2+dj))

    print(len(antinodes))

## P2
def count_antinodes_resonance():
    antinodes = set()
    for k in locations:
        for x in range(len(locations[k])-1):
            for y in range(x+1, len(locations[k])):
                (i1, j1), (i2, j2) = locations[k][x], locations[k][y]
                antinodes.add((i1, j1))
                antinodes.add((i2, j2))
                di, dj = i2-i1, j2-j1
                n = 1
                while is_valid(i1-n*di, j1-n*dj):
                    antinodes.add((i1-n*di, j1-n*dj))
                    n += 1
                n = 1
                while is_valid(i2+n*di, j2+n*dj):
                    antinodes.add((i2+n*di, j2+n*dj))
                    n += 1
    
    print(len(antinodes))




count_antinodes()
count_antinodes_resonance()
