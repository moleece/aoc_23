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
    '''
    sort then convert raw maps input from:
    [['50', '98', '2'], ['52', '50', '48']]
    to:
    [[0, 49, 0], [50, 97, 2], [98, 99, -48]]
    '''
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


def find_destination(source_value, sorted_range):
    for index in range(len(sorted_range)):
        _range = sorted_range[index]

        range_offset = _range[0] - _range[1]

        # handle ranges
        if source_value < _range[1]:
            destination_value = source_value
            # print(destination_value)
            break
        elif source_value >= _range[1] and source_value < (_range[1] + _range[2]):
            destination_value = source_value + range_offset
            # print(destination_value)
            break
        # checks based on next _range start
        elif index < len(sorted_range)-1:
            if source_value >= (_range[1] + _range[2]) and source_value < sorted_range[index+1][1]:
                destination_value = source_value
                # print(destination_value)
                break
        elif index == len(sorted_range)-1:
            if source_value >= (_range[1] + _range[2]): 
                destination_value = source_value
                # print(destination_value)
                break
            elif source_value >= _range[1] and source_value < (_range[1] + _range[2]):
                destination_value = source_value + range_offset
                # print(destination_value)
                break
    
    return destination_value


def find_final_destination(seed, sorted_maps):
    num_maps = len(sorted_maps)
    location = seed

    i = 0
    while i < num_maps:
        # print(location)
        location = find_destination(location, sorted_maps[i])
        i += 1
    
    return location



    


#map_sources_to_destinations # given input source values, return associated destination values


if __name__ == "__main__":
    seeds, raw_maps = extract(lines) # ['79', '14', '55', '13']
    seeds = [int(seed) for seed in seeds]
    sorted_maps = sort_maps(raw_maps)
    destinations = []

    # part 1
    '''
    for seed in seeds:
        destinations.append(find_final_destination(seed, sorted_maps))

    print(f"min final destination: {min(destinations)}")
    '''


    # part 2
    seed_ranges = []
    for j in range(0, len(seeds), 2):
        seed_ranges.append([seeds[j]])


    for k in range(1, len(seeds), 2):
        for l in range(1, seeds[k], 1):
            seed_num = seeds[k - 1] + l 
            seed_ranges[int(k/2)].append(seed_num)
    
    all_seeds = [item for sublist in seed_ranges for item in sublist]

    for seed in all_seeds:
        destinations.append(find_final_destination(seed, sorted_maps))

    print(f"min final destination: {min(destinations)}")



