import sys

pipeMap = {
    '|': {'s': 's', 'n': 'n'},
    '-': {'e': 'e', 'w': 'w'},
    'L': {'s': 'e', 'w': 'n'},
    'J': {'s': 'w', 'e': 'n'},
    '7': {'n': 'w', 'e': 's'},
    'F': {'n': 'e', 'w': 's'},
    '.': {},
    'S': {'n': 'n', 's':'s', 'e':'e', 'w':'w'}
}

dirMap = {
    # i,j after moving that dir
    's': (1,0),
    'e': (0,1),
    'n': (-1,0),
    'w': (0, -1)
}

# P1
def startPos(pipes):
    for i in range(len(pipes)):
        for j in range(len(pipes)):
            if pipes[i][j] == 'S':
                return (i,j)

def walkPaths(pipes):
    start = startPos(pipes)
    
    for startDir in ['n', 'e', 'w', 's']:
        curDir = startDir
        curPos = start
        path = []
        curPos, curDir, path = step(curPos, curDir, pipes, path)
        while curPos != start and curPos != (-1, -1):
            curPos, curDir, path = step(curPos, curDir, pipes, path)
        if curPos == (-1,-1):
            continue
        else:
            return path

def step(curPos, curDir, pipes, path):
    (di, dj) = dirMap[curDir]
    newPos = (curPos[0]+di, curPos[1] + dj)
    newSymbol = pipes[newPos[0]][newPos[1]]
    if curDir not in pipeMap[newSymbol]:
        return (-1,-1), curDir, []
    else:
        return newPos, pipeMap[newSymbol][curDir], path + [(curPos[0], curPos[1], curDir)]

# P2
rightMap = {
    '|': {'s': ['w'], 'n': ['e']},
    '-': {'e': ['s'], 'w': ['n']},
    'L': {'s': ['w','s'], 'w': []},
    'J': {'s': [], 'e': ['e','s']},
    '7': {'n': ['e', 'n'], 'e': []},
    'F': {'n': [], 'w': ['w', 'n']},
    '.': {},
    'S': {'n': 'n', 's':'s', 'e':'e', 'w':'w'}
}

leftMap = {
    '|': {'s': ['e'], 'n': ['w']},
    '-': {'e': ['n'], 'w': ['s']},
    'L': {'s': [], 'w': ['w','s']},
    'J': {'s': ['e','s'], 'e': []},
    '7': {'n': [], 'e': ['e', 'n']},
    'F': {'n': ['w', 'n'], 'w': []},
    '.': {},
    'S': {'n': [], 's':[], 'e':[], 'w':[]}
}

def replaceStart(pipes, path):
    start = path[0]
    (di, dj) = path[0][0] - path[1][0], path[0][1] - path[1][1]
    dir1 = [x for x in dirMap if dirMap[x] == (di, dj)][0]
    (di, dj) = path[0][0] - path[-1][0], path[0][1] - path[-1][1]
    dir2 = [x for x in dirMap if dirMap[x] == (di, dj)][0]
    print(dir1, dir2)
    for pipe in pipeMap:
        if dir1 in pipeMap[pipe] and dir2 in pipeMap[pipe] and pipe != 'S':
            pipes[start[0]][start[1]] = pipe
            break
    return pipes

def replaceChaff(pipes, pathSet):
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if (i, j) not in pathSet:
                pipes[i][j] = '.'
    return pipes


def countEnclosed(pipes, path):
    pipes = replaceStart(pipes, path)
    pathSet = set([(p[0], p[1]) for p in path])
    pipes = replaceChaff(pipes, pathSet)
    # for p in pipes:
    #     print(''.join(p))
    # Mark right and left
    print(path)
    for x in range(len(path)):
        i = path[x][0]
        j = path[x][1]
        enterDir = path[x-1][2]
        print(x)
        rightDirs = rightMap[pipes[i][j]][enterDir]
        leftDirs = leftMap[pipes[i][j]][enterDir]
        for d in rightDirs:
            (di, dj) = dirMap[d]
            if i + di >= len(pipes) or j + dj >= len(pipes[0]) or i + di < 0 or j + dj < 0:
                continue
            if pipes[i+di][j+dj] == '.':
                pipes[i+di][j+dj] = 'r'
        for d in leftDirs:
            (di, dj) = dirMap[d]
            if i + di >= len(pipes) or j + dj >= len(pipes[0]) or i + di < 0 or j + dj < 0:
                continue
            if pipes[i+di][j+dj] == '.':
                pipes[i+di][j+dj] = 'l'
    # for p in pipes:
    #     print(''.join(p))
    
    # Flood fill
    changed = True
    while changed:
        changed = False
        for i in range(len(pipes)):
            for j in range(len(pipes[0])):
                if pipes[i][j] == '.':
                    for d in dirMap:
                        (di, dj) = dirMap[d]
                        if i + di >= len(pipes) or j + dj >= len(pipes[0]) or i + di < 0 or j + dj < 0:
                            continue
                        if pipes[i+di][j+dj] == 'r':
                            changed = True
                            pipes[i][j] = 'r'
                        elif pipes[i+di][j+dj] == 'l':
                            changed = True
                            pipes[i][j] = 'l'
    # for p in pipes:
    #     print(''.join(p))
                        
    # Find a l or r on border
    innerSide = ''
    for i in range(len(pipes)):
        if pipes[i][0] == 'l' or pipes[i][-1] == 'l':
            innerSide = 'r'
            break
        if pipes[i][0] == 'r' or pipes[i][-1] == 'r':
            innerSide = 'l'
            break
    for i in range(len(pipes[0])):
        if pipes[0][i] == 'l' or pipes[-1][i] == 'l':
            innerSide = 'r'
            break
        if pipes[0][i] == 'r' or pipes[-1][i] == 'r':
            innerSide = 'l'
            break
    
    count = 0
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == innerSide:
                count += 1
    return count




    
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    pipes = []
    for line in lines:
        pipes += [[c for c in line.strip()]]
    path = walkPaths(pipes)
    print(countEnclosed(pipes, path)
)
