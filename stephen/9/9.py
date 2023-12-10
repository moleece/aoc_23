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


def construct_differences_list(list):
    differences_list = []
    for i in range(len(list)- 1):
        differences_list.append(list[i+1] - list[i])

    return differences_list


def build_tree(sequence):
    tree = []
    tree.append(sequence)

    while tree[-1].count(0) < len(tree[-1]) and len(tree[-1]) > 0:
        difference_list = construct_differences_list(tree[-1])
        tree.append(difference_list)

    return tree



if __name__ == "__main__":
    sequences = []
    for line in lines:
        sequence = line.split(' ')
        sequence = [int(x) for x in sequence]
        sequences.append(sequence)

    new_history_values = []

    for sequence in sequences:
        tree = build_tree(sequence)

        tree[-1].append(0)

        for i in range(-2, -len(tree)-1, -1):
            tree[i].append(tree[i][-1] + tree[i+1][-1])

        new_history_values.append(tree[0][-1])

    print(sum(new_history_values))


