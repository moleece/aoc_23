# python 1.py input.txt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# recursive solution:
# parse line, find nums and their positions, find symbols and their positions
# parse next line, find symbols and their positions
# check for adjacency between current line numbers and any symbols, add to total
# check next line

# base case, final line reached and parsed

# .....+.58.

def extract_positions(line):
    # 617*......
    # ['617']
    # [[0, 1, 2]]
    # [3]    
    line_nums = []
    num_indices = []
    symbol_indices = []
    for i in range(len(line)):
        if line[i].isdigit() and (not num_indices or num_indices[-1].count(i-1) == 0):
            line_nums.append(line[i])
            num_indices.append([i])
        elif line[i].isdigit() and (not num_indices or num_indices[-1].count(i-1) != 0):
            line_nums[-1] += line[i]
            num_indices[-1].append(i)
        elif line[i] != '.':
            symbol_indices.append(i)
    
    return { 'line_nums': line_nums, 'num_indices': num_indices, 'symbol_indices': symbol_indices }


def increment_and_remove_num(line_index, line_nums_index, all_positions):
    if all_positions[line_index]['line_nums']:
        print('removing ' + all_positions[line_index]['line_nums'][line_nums_index])
        print(all_positions[line_index])
        all_positions['total'] += int(all_positions[line_index]['line_nums'][line_nums_index])
        all_positions[line_index]['line_nums'][line_nums_index] = '0'
        # all_positions[line_index]['num_indices'][line_nums_index] = []

    # show_all_positions(all_positions)
    print(all_positions[line_index])
    print('total after num removed')
    print(all_positions['total'])

    return all_positions


#check_nums(line_index, symbol_index, all_positions):
#    for num_index in range(len(all_positions[line_index]['line_nums'])):

def check_nums_prev_line(line_index, symbol_index, all_positions):
    prev_line_index = line_index - 1
    for index in range(len(all_positions[prev_line_index]['line_nums'])):
        for digit_index in all_positions[prev_line_index]['num_indices'][index]:
            if digit_index == symbol_index - 1 or digit_index == symbol_index or digit_index == symbol_index + 1:
                all_positions = increment_and_remove_num(prev_line_index, index, all_positions)

    return all_positions


def check_nums_current_line(line_index, symbol_index, all_positions):
    for index in range(len(all_positions[line_index]['line_nums'])):
        for digit_index in all_positions[line_index]['num_indices'][index]:
            if digit_index == symbol_index - 1 or digit_index == symbol_index + 1:
                all_positions = increment_and_remove_num(line_index, index, all_positions)

    return all_positions


def check_nums_next_line(line_index, symbol_index, all_positions):
    next_line_index = line_index + 1
    for index in range(len(all_positions[next_line_index]['line_nums'])):
        for digit_index in all_positions[next_line_index]['num_indices'][index]:
            if digit_index == symbol_index - 1 or digit_index == symbol_index or digit_index == symbol_index + 1:
                all_positions = increment_and_remove_num(next_line_index, index, all_positions)

    return all_positions


def extract_symbol_adjacencies(line_index, symbol_index, all_positions):
    # given a line index and symbol index, find all numbers that are touching that symbol
    # add numbers to running total
    # remove numbers from all_positions so they can't be double counted

    # TODO refactor to only use one check nums function and call it with line_index - 1, line_index, or line_index + 1
    if line_index == 0:
        all_positions = check_nums_current_line(line_index, symbol_index, all_positions)
        all_positions = check_nums_next_line(line_index, symbol_index, all_positions)

    if line_index == len(all_positions)-2: # 2 because 'total' is a key in all_positions
        all_positions = check_nums_prev_line(line_index, symbol_index, all_positions)
        all_positions = check_nums_current_line(line_index, symbol_index, all_positions)

    if line_index > 0:
        all_positions = check_nums_prev_line(line_index, symbol_index, all_positions)
        all_positions = check_nums_current_line(line_index, symbol_index, all_positions)
        all_positions = check_nums_next_line(line_index, symbol_index, all_positions)

    return all_positions
    

def show_all_positions(all_positions):
    for key in all_positions.keys():
        print('line: ' + str(key))
        print('all_positions: ' + str(all_positions[key]))


##### Part 2


def extract_positions2(line):
    line_nums = []
    num_indices = []
    symbol_indices = []
    for i in range(len(line)):
        if line[i].isdigit() and (not num_indices or num_indices[-1].count(i-1) == 0):
            line_nums.append(line[i])
            num_indices.append([i])
        elif line[i].isdigit() and (not num_indices or num_indices[-1].count(i-1) != 0):
            line_nums[-1] += line[i]
            num_indices[-1].append(i)
        elif line[i] == '*':
            symbol_indices.append(i)
    
    return { 'line_nums': line_nums, 'num_indices': num_indices, 'symbol_indices': symbol_indices }


def extract_gear_adjacencies(line_index, symbol_index, all_positions):
    adjacency_count = 0
    gear_numbers = []
    gear_ratio = 0
    if line_index == 0:
        current_line_adjacency_count, current_numbers = check_adjacent_locations(line_index, symbol_index, all_positions)
        next_line_adjacency_count, next_numbers = check_adjacent_locations(line_index + 1, symbol_index, all_positions)

        adjacency_count = current_line_adjacency_count + next_line_adjacency_count
        gear_numbers = current_numbers + next_numbers

    if line_index == len(all_positions)-1:
        prev_line_adjacency_count, prev_numbers = check_adjacent_locations(line_index - 1, symbol_index, all_positions)
        current_line_adjacency_count, current_numbers = check_adjacent_locations(line_index, symbol_index, all_positions)

        adjacency_count = prev_line_adjacency_count + current_line_adjacency_count
        gear_numbers = prev_numbers + current_numbers

    if line_index > 0:
        prev_line_adjacency_count, prev_numbers = check_adjacent_locations(line_index - 1, symbol_index, all_positions)
        current_line_adjacency_count, current_numbers = check_adjacent_locations(line_index, symbol_index, all_positions)
        next_line_adjacency_count, next_numbers = check_adjacent_locations(line_index + 1, symbol_index, all_positions)

        adjacency_count = prev_line_adjacency_count + current_line_adjacency_count + next_line_adjacency_count
        gear_numbers = prev_numbers + current_numbers + next_numbers

    print('line adjacency for line ' + str(line_index))
    print(adjacency_count)
    print('gear numbers ' + str(gear_numbers))
    if adjacency_count == 2:
        gear_ratio += gear_numbers[0] * gear_numbers[1]

    return gear_ratio


def check_adjacent_locations(line_index, symbol_index, all_positions):
    line_nums_adjacent = 0
    nums = []
    print('symbol index: ' + str(symbol_index))
    for i in range(len(all_positions[line_index]['line_nums'])):
        num = int(all_positions[line_index]['line_nums'][i])
        num_indices = all_positions[line_index]['num_indices'][i]
        if (symbol_index-1 in num_indices) or (symbol_index in num_indices) or (symbol_index+1 in num_indices):
            line_nums_adjacent += 1
            nums.append(num)
    
    return line_nums_adjacent, nums


if __name__ == "__main__":
    for line in lines:
        print(line)
    all_positions = {}
    # all_positions['total'] = 0

    for index, line in enumerate(lines):
        # all_positions[index] = extract_positions(line)
        all_positions[index] = extract_positions2(line)

    # for index, line in enumerate(lines):
        # for i in range(len(all_positions[index]['symbol_indices'])):
            # print('symbol in line line ' + str(index) + ', ' + line)
            # all_positions = extract_symbol_adjacencies(index, all_positions[index]['symbol_indices'][i], all_positions)

    gear_ratio_sum = 0

    for index, line in enumerate(lines):
        for i in range(len(all_positions[index]['symbol_indices'])):
            symbol_index = all_positions[index]['symbol_indices'][i]
            gear_ratio_sum += extract_gear_adjacencies(index, symbol_index, all_positions)

    # print('total')
    # print(all_positions['total'])

    print('gear ratio sum')
    print(gear_ratio_sum)
