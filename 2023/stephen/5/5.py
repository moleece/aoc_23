# python 1.py input.txt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

humidity-to-location map:
60 56 37
56 93 4

destination range start, source range start, range length

50 98 2
52 50 48
seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51

find if/which range a given source value falls into:

0 to start of first source number - (offset = 0)
first source number to that plus range - (offset = +2) in case 1
that to next source number - (offset = 0)
that to that + associated range - (offset = -48)  in case 1
etc.
above last source number + it's range - (offset = 0)

for any source destination pair, calculate the offset, (+, 0 , - value)

find which range the source value falls into, then add the associated offset

'''

def extract(lines):
    raw_maps = []
    seeds = lines[0].split(' ')[1:]

    for line in lines:
        if line.find('map') != -1:
            raw_maps.append([])
        elif len(raw_maps) > 0 and len(line.strip()) > 0:
            raw_maps[-1].append(line.split(' '))

    return seeds, raw_maps


def sort_maps(raw_maps): # (source start, source end, offset)
    converted_data = [[[int(value) for value in inner_list] for inner_list in outer_list] for outer_list in raw_maps]
    sorted_maps = [sorted(outer_list, key=lambda x: x[1]) for outer_list in converted_data]
    '''
    [
      [[52, 50, 48], [50, 98, 2]]
      [[39, 0, 15], [0, 15, 37], [37, 52, 2]]
      [[42, 0, 7], [57, 7, 4], [0, 11, 42], [49, 53, 8]]
      [[88, 18, 7], [18, 25, 70]]
      [[81, 45, 19], [68, 64, 13], [45, 77, 23]]
      [[1, 0, 69], [0, 69, 1]]
      [[60, 56, 37], [56, 93, 4]]   
    [
    '''
    return sorted_maps


def process_map(sorted_map):
    offset_ranges = []
    offset_range_offsets = []

    for j in range(len(sorted_map)):
        offset_ranges.append([sorted_map[j][1], sorted_map[j][1] + sorted_map[j][2]-1])
        offset_range_offsets.append(sorted_map[j][0] - sorted_map[j][1])

    return offset_ranges, offset_range_offsets

def process_maps(sorted_maps):
    all_offset_ranges = []
    all_offset_range_offsets = []

    for i in range(len(sorted_maps)):
        offset_range, offset_range_offsets = process_map(sorted_maps[i])

        all_offset_ranges.append(offset_range)
        all_offset_range_offsets.append(offset_range_offsets)

    return all_offset_ranges, all_offset_range_offsets


def map_to_destination(source_value, offset_ranges, offset_range_offsets):
    # iterate over ranges within map
    for i in range(len(offset_ranges)):
        # early returns are not correct
        if source_value < offset_ranges[0][0]:
            return source_value

        if source_value > offset_ranges[-1][-1]:
            return source_value

        if source_value >= offset_ranges[i][0] and source_value <= offset_ranges[i][1]:
            return source_value + offset_range_offsets[i]

        if source_value < offset_ranges[i][0]:
            return source_value
    
    return source_value


def map_to_final_destination(source_value, all_offset_ranges, all_offset_range_offsets):
    '''
    for each set of offset ranges, find which range the source fits in
        if between ranges, offset = 0
        if within a range, offset = offset range offset
    if final source location < current min location, update min location
    '''
    value = source_value
    # iterate over all maps 
    for i in range(len(all_offset_ranges)):
        offset_range = all_offset_ranges[i]
        offset_range_offsets = all_offset_range_offsets[i]

        value = map_to_destination(value, offset_range, offset_range_offsets)

    return value





if __name__ == "__main__":
    seeds, raw_maps = extract(lines) # ['79', '14', '55', '13']
    seeds = [int(seed) for seed in seeds]
    seeds_count = len(seeds)
    sorted_maps = sort_maps(raw_maps)
    destinations = []

    # part 1
    '''
    for seed in seeds:
        destinations.append(find_final_destination(seed, sorted_maps))

    print(f"min final destination: {min(destinations)}")
    '''

    # part 2
    current_min_location = 10000000000
    all_offset_ranges, all_offset_range_offsets = process_maps(sorted_maps)

    for i in range(0, len(seeds), 2):
        for j in range(0, seeds[i+1], 1):
            destination = map_to_final_destination( seeds[i]+j, all_offset_ranges, all_offset_range_offsets)
            if destination < current_min_location:
                current_min_location = destination

    print(current_min_location)
