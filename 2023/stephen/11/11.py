# python 1.py input.txt
import math
import argparse
import re
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()
with open(args.input_file, 'r') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

'''
Expand the universe, then find the length of the shortest path between every pair of galaxies.
What is the sum of these lengths?
'''

'''
expand universe:
- convert image into numpy matrix of 1s and 0s
- iterate over rows, find rows without galaxies, insert empty row for each empty row
- rotate matrix
- iterate over rows...


find paths:
- iterate over rows, identify coordinates of all galaxies
- construct all unique pairings of galaxies
- calculate distance for each pairing
- sum distances
'''

'''
for part 2, universe is expanded by a factor of 1 million instead of 2
- don't construct an expanded universe, 
  instead build map of columns/rows of image that are empty
- when calculating distance, find intersection of rows/columns travelled with 
  empty columns/rows
  (note that it's not possible for start/end rows/columns to be empty)
- d = (old d calculation - num intersections) + (num intersections * 1mil)
OR
- when calc d, iterate over rows travelled (per dimension x/y),
  if row empty, add 1mil, else add 1
- could memoize row emptiness for each dimension
'''

def expand_row_wise(image, expanded_universe):
    for row in image:
        if row.count(0) == len(row):
            expanded_universe.append(row)
            expanded_universe.append(row)
        else:
            expanded_universe.append(row)

    return expanded_universe


def find_galaxy_coordinates(universe, galaxy_coordinates):
    for index, row in enumerate(universe):
        if row.count(0) == len(row):
            continue

        for i in range(len(row)):
            if row[i] == 1:
                galaxy_coordinates.append([index, i])

    return galaxy_coordinates


def create_pairings(galaxy_coordinates):
    paths = []
    for j in range(0, len(galaxy_coordinates) - 1):
        for k in range(1, len(galaxy_coordinates) - j):
            paths.append([galaxy_coordinates[j], galaxy_coordinates[j + k]])

    return paths

# part 1
def calculate_distance(path):
    coord_1 = path[0]
    coord_2 = path[1]
    d = abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1]) 

    return d

# part 2
def calculate_distance_1d(start_stop, image_ary):
    d = 0
    for i in range(start_stop[0], start_stop[1]):
        if image_ary[i].sum() == 0:
            d += 1000000
        else:
            d += 1

    return d

    




if __name__ == "__main__":
    image = []
    for line in lines:
        image.append([])
        for letter in line:
            image[-1].append(0) if letter == '.' else image[-1].append(1)

    '''
    # part 1
    x_expanded_universe = []
    x_expanded_universe = expand_row_wise(image, x_expanded_universe)
    # rotate x expanded universe
    x_expanded_universe_array = np.array(x_expanded_universe)
    x_expanded_universe_transposed_array = x_expanded_universe_array.T
    x_expanded_universe = x_expanded_universe_transposed_array.tolist()
    print('x expanded universe')
    for row in x_expanded_universe:
        print(row)
    y_expanded_universe = []
    y_expanded_universe = expand_row_wise(x_expanded_universe, y_expanded_universe)
    
    fully_expanded_universe = y_expanded_universe
    print('fully expanded')
    for row in fully_expanded_universe:
        print(row)
    galaxy_coordinates = []
    galaxy_coordinates = find_galaxy_coordinates(fully_expanded_universe, galaxy_coordinates)
    paths = create_pairings(galaxy_coordinates)
    print(f"paths length: {len(paths)}")
    total_distance = 0
    for path in paths:
        total_distance += calculate_distance(path)
    print(f"total distance {total_distance}")
    '''

    # part 2
    # build matrix for x component
    # build matrix for y component
    # do distance calculation for each row of both components
    image_ary = np.array(image)
    rotated_image_ary = image_ary.T
    rotated_image = rotated_image_ary.tolist()

    galaxy_coordinates = []
    galaxy_coordinates = find_galaxy_coordinates(image, galaxy_coordinates)
    paths = create_pairings(galaxy_coordinates)
    total_distance = 0

    for path in paths:
        x_start_stop = [min([path[0][0], path[1][0]]), max([path[0][0], path[1][0]])]
        y_start_stop = [min([path[0][1], path[1][1]]), max([path[0][1], path[1][1]])]

        total_distance += calculate_distance_1d(x_start_stop, image_ary)
        total_distance += calculate_distance_1d(y_start_stop, rotated_image_ary)

    print('total d')
    print(total_distance)
