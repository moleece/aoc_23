# python 1.py input.txt
import math
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()
with open(args.input_file, 'r') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

heading_acceptable_tiles = {
    'north': ['S', 'F', '|', '7'],
    'east': ['S', 'J', '-', '7'],
    'south': ['S', 'J', '|', 'L'],
    'west': ['S', '-', 'L', 'F']
}

tile_previous_heading_map = {
    '|': {'north': 'north', 'south': 'south'},
    '-': {'east': 'east', 'west': 'west'},
    'L': {'south': 'east', 'west': 'north'},
    'J': {'south': 'west', 'east': 'north'},
    '7': {'north': 'west', 'east': 'south'},
    'F': {'north': 'east', 'west': 'south'},
    '.': {'north': 'end', 'south': 'end', 'east': 'end', 'west': 'end'}
}


def explore_initial_direction(s_position, direction, traversed_tiles):
    '''
    traverse a potential path
    if s_position is reached, loop found
    if dead end reached, explore next possible path
    keep track current heading (initially initial direction and subsequently current direction)
    maintain current distance traveled
    maintain hash of distance: position so that you can find the position at d/2
    (it is possible that there are two possible loops)
    (I might hardcode the correct direction since it can be determined by inspection for part 1)
    '''
    travelling = True
    distance = -1
    position = s_position
    is_loop = False

    # take one step before entering while loop
    traversed_tiles[position[0]].append(position[1])
    position, direction, distance, travelling = travel(position, direction, distance)

    while travelling and position != s_position:
        traversed_tiles[position[0]].append(position[1])
        position, direction, distance, travelling = travel(position, direction, distance)
        if direction == 'loop':
            is_loop = True

        if direction == 'end':
            is_loop = False
            travelling = False

    return distance, is_loop


def travel(current_position, current_direction, distance):
    travelling = True
    next_position = calculate_next_position(current_position, current_direction)
    traversable, new_heading = check_position_and_heading(next_position, current_direction)

    if traversable == False:
        travelling = False
    else: 
        distance += 1

    if new_heading == 'loop':
        travelling = False

    return next_position, new_heading, distance, travelling


def calculate_next_position(current_position, current_direction):
    y, x = current_position[0], current_position[1]
    
    if current_direction == 'north':
        y -= 1
    elif current_direction == 'east':
        x += 1
    elif current_direction == 'south':
        y += 1
    elif current_direction == 'west':
        x -= 1

    return [y, x]


def check_position_and_heading(position, previous_direction):
    traversable = True
    y, x = position[0], position[1]
    position_tile = grid[y][x]
    new_heading = 'end'

    if x < 0 or x >= grid_width or y < 0 or y >= grid_height:
        traversable = False
        return traversable, new_heading

    if position_tile == '.':
        traversable = False
        return traversable, 'end'

    if position_tile not in heading_acceptable_tiles[previous_direction]:
        traversable = False
        return traversable, new_heading

    if position_tile == 'S':
        print('S tile reached!!!')
        return traversable, 'loop'
    else:
        # print(f"position tile: {position_tile}, previous_direction: {previous_direction}")
        # print(tile_previous_heading_map[position_tile])
        new_heading = tile_previous_heading_map[position_tile][previous_direction]

    return traversable, new_heading


def count_enclosed_in_row(indexes_traversed, y, grid):
    vertical_component_pipes = ['L', '|', 'F', '7', 'J', 'S'] # S by inspection, not generalized
    counting = False
    total = 0
    
    for n in range(len(indexes_traversed)-1):
        for i in range(indexes_traversed[n], indexes_traversed[n+1]+1):
            tile_value = grid[y][i]

            if i in indexes_traversed and tile_value in vertical_component_pipes:
                counting = not counting
                continue

            if i in indexes_traversed and tile_value not in vertical_component_pipes:
                continue

            if not counting:
                continue
            
            total += 1
    # print(f"count for row {i}: {total}")

    return total


if __name__ == "__main__":
    grid = lines # grid[y][x] top left to bottom right
    grid_width = len(grid[0])
    grid_height = len(grid)

    s_position = []

    '''
    keep a hash of grid row to positions traversed and pipe type
    iterate over grid
        iterate over positions between the first position and last position traversed by loop
            - add positions to total when the number of counted pipes is odd (start with at count = 1)
            - don't add horizontal pipes to total and also don't count them as switches 
              (only switch on pipes with vertical component that were traversed)

    '''
    # for part 2
    traversed_tiles = [] # list (y's) of hashes (x of pipe traversed to pipe type)
    for i in range(grid_height):
        traversed_tiles.append([])

    # find S position
    for i in range(len(grid)):
        if grid[i].find('S') != -1:
            s_position.append(i)
            s_position.append(grid[i].index('S'))

    # part 1, initial direction determined by inspection
    initial_direction = 'south'

    distance, is_loop = explore_initial_direction(s_position, initial_direction, traversed_tiles)

    half_distance = math.ceil(distance/2)
    print(f"DONE half distance: {half_distance}, is_loop: {is_loop}")


    # part 2
    total_enclosed = 0

    for i in range(grid_height):
        traversed_tiles[i].sort()

    print(traversed_tiles)

    for i in range(grid_height):
        if len(traversed_tiles[i]) == 0:
            continue

        total_enclosed += count_enclosed_in_row(traversed_tiles[i], i, grid)

    print(f"total_enclosed: {total_enclosed}")


