import sys
import functools
from heapq import *


revMap = {'n': 's', 's': 'n', 'w': 'e', 'e':'w'}
dirPosChange = {'n':(-1,0),
          's':(1,0),
          'w':(0,-1),
          'e':(0,1)}

# P1
def dijkstra3(grid):
    visited = []
    for i in range(len(grid)):
        newRow = []
        for j in range(len(grid[0])):
            newRow += [set()]
        visited += [newRow]
    h = sorted([(grid[0][1], 0, 1, 'e1'), (grid[1][0], 1, 0, 's1')]) # (dist, i, j, travelDir)
    nextElem = heappop(h)
    while nextElem[1] != len(grid) - 1 or nextElem[2] != len(grid[0]) - 1:
        (travelDist, i, j, travelDir) = nextElem
        if travelDir not in visited[i][j]:
            visited[i][j].add(travelDir)
            # Add neighbors
            compassDir = travelDir[0]
            consecSteps = int(travelDir[1])
            dirOptions = set(['n', 'e', 'w', 's'])
            dirOptions.remove(revMap[compassDir])
            if consecSteps >= 3:
                dirOptions.remove(compassDir)
            for newDir in dirOptions:
                newSteps = 1
                if newDir == compassDir:
                    newSteps = consecSteps + 1
                (di, dj) = dirPosChange[newDir]
                if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j + dj >= len(grid[0]):
                    continue
                heappush(h, (travelDist+grid[i+di][j+dj], i+di, j+dj, newDir+str(newSteps)))
        nextElem = heappop(h)
    return nextElem

# P2
def dijkstra4_10(grid):
    visited = []
    for i in range(len(grid)):
        newRow = []
        for j in range(len(grid[0])):
            newRow += [set()]
        visited += [newRow]
    h = sorted([(grid[0][1], 0, 1, 'e1'), (grid[1][0], 1, 0, 's1')]) # (dist, i, j, travelDir)
    nextElem = heappop(h)
    while nextElem[1] != len(grid) - 1 or nextElem[2] != len(grid[0]) - 1 or int(nextElem[3][1:]) < 4:
        (travelDist, i, j, travelDir) = nextElem
        if travelDir not in visited[i][j]:
            visited[i][j].add(travelDir)
            # Add neighbors
            compassDir = travelDir[0]
            consecSteps = int(travelDir[1:])
            dirOptions = set(['n', 'e', 'w', 's'])
            dirOptions.remove(revMap[compassDir])
            if consecSteps < 4:
                dirOptions = set([compassDir])
            if consecSteps >= 10:
                dirOptions.remove(compassDir)
            for newDir in dirOptions:
                newSteps = 1
                if newDir == compassDir:
                    newSteps = consecSteps + 1
                (di, dj) = dirPosChange[newDir]
                if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j + dj >= len(grid[0]):
                    continue
                heappush(h, (travelDist+grid[i+di][j+dj], i+di, j+dj, newDir+str(newSteps)))
        nextElem = heappop(h)
    return nextElem

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

    grid = [list(map(int, line)) for line in lines]
    # print(grid)
    total = dijkstra4_10(grid)
    print(total)
    