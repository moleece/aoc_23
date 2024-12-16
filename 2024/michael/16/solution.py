import sys, math



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    
    adjLists = {}
    directions = ['>', 'v', '<', '^']
    directionDeltas = {'>': (0,1), 'v': (1,0), '<': (0,-1), '^': (-1,0)}
    dirNeighbors = {'>': ['^', 'v'], 'v': ['<', '>'], '<': ['v', '^'], '^': ['>', '<']}
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '#':
                continue
            for direction in directions:
                adjLists[(i, j, direction)] = []
                di, dj = directionDeltas[direction]
                if grid[i+di][j+dj] != '#':
                    adjLists[(i, j, direction)].append((i+di, j+dj, direction, 1))
                for newDirection in dirNeighbors[direction]:
                    adjLists[(i, j, direction)].append((i, j, newDirection, 1000))
    
    # Dijkstra's algorithm
    dist = {}
    for key in adjLists:
        dist[key] = math.inf
    dist[(start[0], start[1], '>')] = 0

    visited = set()
    parents = {}
    minDist = 100
    while minDist <= 95476:
    # while len(visited) < len(adjLists):
        minDist = math.inf
        minNode = None
        for key in dist:
            if key not in visited and dist[key] < minDist:
                minDist = dist[key]
                minNode = key
        visited.add(minNode)
        for neighbor in adjLists[minNode]:
            if dist[minNode] + neighbor[3] < dist[(neighbor[0], neighbor[1], neighbor[2])]:
                dist[(neighbor[0], neighbor[1], neighbor[2])] = dist[minNode] + neighbor[3]
                parents[(neighbor[0], neighbor[1], neighbor[2])] = [minNode]
            elif dist[minNode] + neighbor[3] == dist[(neighbor[0], neighbor[1], neighbor[2])]:
                parents[(neighbor[0], neighbor[1], neighbor[2])].append(minNode)

   
    print(min([dist[(end[0], end[1], d)] for d in directions]))

    # Backtrack using parents            
    cells = set()
    good_nodes = [(end[0], end[1], d) for d in directions if (end[0], end[1], d) in parents]

    while good_nodes:
        n = good_nodes.pop()
        cells.add((n[0], n[1]))
        try:
            for parent in parents[n]:
                good_nodes.append(parent)
        except:
            continue
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in cells:
                grid[i][j] = 'O'
        print(''.join(grid[i]))
    print(len(cells))

    