import sys


def get_regions(grid):
    regions = []
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j]:
                continue
            region = set()
            stack = [(i, j)]
            perimeter = 0
            while stack:
                m, n = stack.pop()
                if (m,n) in region:
                    continue
                if grid[m][n] != grid[i][j]:
                    continue
                region.add((m,n))
                visited[m][n] = True
                if m > 0:
                    stack.append((m-1, n))
                if m < len(grid) - 1:
                    stack.append((m+1, n))
                if n > 0:
                    stack.append((m, n-1))
                if n < len(grid[0]) - 1:
                    stack.append((m, n+1))
            if len(region) >= 1:
                regions.append((grid[i][j], region))
    
    return regions


def get_perimeter(region):
    perimeter = 0
    for i, j in region:
        if i == 0 or (i-1, j) not in region:
            perimeter += 1
        if i == len(grid) - 1 or (i+1, j) not in region:
            perimeter += 1
        if j == 0 or (i, j-1) not in region:
            perimeter += 1
        if j == len(grid[0]) - 1 or (i, j+1) not in region:
            perimeter += 1
    return perimeter

def get_num_edges(region):
    # Now colinear edges only count as one edge
    edges = set()
    for i, j in region:
        if i == 0 or (i-1, j) not in region:
            edges.add((i, j, 'up'))
        if i == len(grid) - 1 or (i+1, j) not in region:
            edges.add((i, j, 'down'))
        if j == 0 or (i, j-1) not in region:
            edges.add((i, j, 'left'))
        if j == len(grid[0]) - 1 or (i, j+1) not in region:
            edges.add((i, j, 'right'))

    connected_edges = []
    while len(edges) > 0:
        edge = edges.pop()
        connected_edges += [edge]
        i, j, direction = edge
        # Now we need to remove all edges that are connected to this edge in the same direction
        if direction == 'up':
            to_remove = set([(i, j-1, 'up'), (i, j+1, 'up')]).intersection(edges)
            while to_remove:
                new_remove = set()
                for remove_edge in to_remove:
                    edges.remove(remove_edge)
                    (m, n, d) = remove_edge
                    new_remove.update([(m, n-1, 'up'), (m, n+1, 'up')])
                to_remove = new_remove.intersection(edges)
        elif direction == 'down':
            to_remove = set([(i, j-1, 'down'), (i, j+1, 'down')]).intersection(edges)
            while to_remove:
                new_remove = set()
                for remove_edge in to_remove:
                    edges.remove(remove_edge)
                    (m, n, d) = remove_edge
                    new_remove.update([(m, n-1, 'down'), (m, n+1, 'down')])
                to_remove = new_remove.intersection(edges)
        elif direction == 'left':
            to_remove = set([(i-1, j, 'left'), (i+1, j, 'left')]).intersection(edges)
            while to_remove:
                new_remove = set()
                for remove_edge in to_remove:
                    edges.remove(remove_edge)
                    (m, n, d) = remove_edge
                    new_remove.update([(m-1, n, 'left'), (m+1, n, 'left')])
                to_remove = new_remove.intersection(edges)
        elif direction == 'right':
            to_remove = set([(i-1, j, 'right'), (i+1, j, 'right')]).intersection(edges)
            while to_remove:
                new_remove = set()
                for remove_edge in to_remove:
                    edges.remove(remove_edge)
                    (m, n, d) = remove_edge
                    new_remove.update([(m-1, n, 'right'), (m+1, n, 'right')])
                to_remove = new_remove.intersection(edges)
        
       
    return connected_edges



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    grid = [list(line.strip()) for line in lines]
    regions = get_regions(grid)
    
    # P1
    total = 0
    for color, region in regions:
        # print(color, len(region), get_perimeter(region))
        total += get_perimeter(region) * len(region)
    # print(total)

    # P2
    total = 0
    for color, region in regions:
        # print(color, len(region), get_num_edges(region))
        total += len(get_num_edges(region)) * len(region)
    print(total)