import sys



def sim_fall(grid, blocks):
    for x, y in blocks:
        grid[y][x] = '#'
    return grid

def dijkstra(grid, start, end):
    queue = [(0, start)]
    visited = set()
    while queue:
        cost, (x, y) = queue.pop(0)
        if (x, y) == end:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                continue
            if grid[ny][nx] == '#':
                continue
            queue.append((cost + 1, (nx, ny)))
    print('No path found')
    return -1



if __name__ == '__main__':
    dim = 71
    grid = [['.' for _ in range(dim)] for _ in range(dim)]
    blocks = []
    with open(sys.argv[1]) as f:
        for line in f:
            x, y = map(int, line.split(','))
            blocks.append((x, y))
    
    for j in range(1024, 3000):
        grid = [['.' for _ in range(dim)] for _ in range(dim)]
        grid = sim_fall(grid, blocks[:j])

        if dijkstra(grid, (0, 0), (dim-1, dim-1)) == -1:
            print(blocks[j-1])
            break