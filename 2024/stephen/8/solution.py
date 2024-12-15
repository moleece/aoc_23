import sys
from typing import List, Dict

grid = []
frequency_nodes: Dict[str, set] = {}

with open(sys.argv[1]) as f:
    for y, line in enumerate(f.readlines()):
        grid.append(line.strip())
        for x, char in enumerate(line.strip()):
            if frequency_nodes.get(char, set()):
                frequency_nodes[char].add((y,x))
            elif char != '.':
                frequency_nodes[char] = set()
                frequency_nodes[char].add((y,x))
            else:
                continue

grid_size = (len(grid), len(grid[0])) # (y height, x width)

def calculate_antinode(center, pair_node, i) -> set:
    x = center[1] + (i * (center[1] - pair_node[1]))
    y = center[0] + (i * (center[0] - pair_node[0]))
    return (y, x)

def in_grid(coordinate):
    if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] >= grid_size[0] or coordinate[1] >= grid_size[1]:
        return False
    return True

antinodes = {}

for freq in frequency_nodes:
    nodes = frequency_nodes[freq]
    antinodes[freq] = set()

    for node in nodes:
        current_node = node
        other_nodes = nodes - {node}

        for other_node in other_nodes:
            i = 1
            while in_grid(calculate_antinode(current_node, other_node, i)):
                antinodes[freq].add(calculate_antinode(current_node, other_node, i))
                i += 1

all_harmonics = set()

for freq in antinodes:
    all_harmonics = all_harmonics.union(antinodes[freq])
    all_harmonics = all_harmonics.union(frequency_nodes[freq])

print(len(all_harmonics))
