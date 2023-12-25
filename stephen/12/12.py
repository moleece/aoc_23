# python 1.py input.txt
import argparse
import functools

from numpy import block, who
from numpy.lib.shape_base import row_stack

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()
with open(args.input_file, 'r') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

'''
@functools.cache
OPT(i,j): the number of possibilities past i where the j-th block starts exactly at position i 


blocks = [1, 2]

'''

@functools.cache
def opt(i, j, row_map, row_blocks):
    # print(f"{i},{j}")
    block_length = row_blocks[j]
    map_length = len(row_map)
    possibilities = 0

    if i + block_length > map_length:
        return 0
    
    for n in range(i, i + block_length):
        if row_map[n] == '.':
            return 0

    if i + block_length < map_length and row_map[i + block_length] == '#':
        return 0

    if j == len(row_blocks)-1:
        if row_map[i + block_length:].find('#') != -1:
            return 0

        return 1

    for x in range(i + block_length + 1, map_length):
        possibilities += opt(x, j+1, row_map, row_blocks)
        if row_map[x] == '#':
            break

    return possibilities 


if __name__ == "__main__":
    print(lines)
    maps = []
    blocks = []
    for line in lines:
        split = line.split(' ')
        maps.append(split[0])
        row_blocks = []
        for i in split[1].split(','):
            row_blocks.append(int(i))
        blocks.append(tuple(row_blocks))

    possibilities= 0
    j = 0
    x = 0

    row_num = 1
    
    for y in range(len(maps)):

        row_map = '?'.join([maps[y]]*5)
        row_blocks = blocks[y]*5
        p = 0
        
        for x in range(len(row_map)):
            p += opt(x, j, row_map, row_blocks)

            possibilities += opt(x, j, row_map, row_blocks)
            if row_map[x] == '#':
                break

        print(row_map, row_blocks, p)
    print('possibilities')
    print(possibilities)
