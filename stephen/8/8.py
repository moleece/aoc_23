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


def parse_lines(lines):
    '''
    'LR'
    {'AAA': ['BBB', 'CCC'], 
    'BBB': ['DDD', 'EEE'], 
    'CCC': ['ZZZ', 'GGG']...}
    '''
    instructions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        line = lines[i].replace('= ', '').replace('(', '').replace(')', '').replace(',', '').split(' ')
        nodes[line[0]] = [line[1], line[2]]

    return instructions, nodes


def parse_lines_2(lines):
    keys = []
    instructions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        line = lines[i].replace('= ', '').replace('(', '').replace(')', '').replace(',', '').split(' ')
        nodes[line[0]] = [line[1], line[2]]
        keys.append(line[0])

    return instructions, nodes, keys


def travel(current_node_key, current_instruction, nodes):
    index = 0
    if current_instruction == 'R':
        index = 1

    new_node_key = nodes[current_node_key][index]

    return new_node_key


def travel_nodes(current_node_keys, current_instruction, nodes):
    for i in range(len(current_node_keys)):
        current_node_keys[i] = travel(current_node_keys[i], current_instruction, nodes)

    return current_node_keys


def continue_travelling(current_node_keys):
    for i in range(len(current_node_keys)):
        if current_node_keys[i][-1] != 'Z':
            return True

    return False


if __name__ == "__main__":
    # instructions, nodes = parse_lines(lines)
    instructions, nodes, keys = parse_lines_2(lines)
    total_steps = 0
    # current_node_key = 'AAA'
    current_instruction_i = 0
    total_instructions = len(instructions)
    travelling = True

    current_node_keys = []
    for key in keys:
        if key[2] == 'A':
            current_node_keys.append(key)

    print('current node keys')
    print(current_node_keys)
    print('nodes count')
    print(len(nodes))


    while travelling:
        total_steps += 1
        if current_instruction_i >= total_instructions:
            current_instruction_i = 0

        current_instruction = instructions[current_instruction_i]
        current_node_keys = travel_nodes(current_node_keys, current_instruction, nodes)

        current_instruction_i += 1
        travelling = continue_travelling(current_node_keys)


    print(total_steps)


    '''
    part 1
    while current_node_key != 'ZZZ':
        print('current node key, instruction index, total steps')
        print(current_node_key)
        print(current_instruction_i)
        print(total_steps)

        total_steps += 1
        
        if current_instruction_i >= total_instructions:
            current_instruction_i = 0
        
        current_instruction = instructions[current_instruction_i]
        
        current_node_key = travel(current_node_key, current_instruction, nodes)
        current_instruction_i += 1
    '''


