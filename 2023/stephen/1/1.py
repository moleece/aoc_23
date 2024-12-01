# python 1.py input.txt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()


def parseLine(line):
    total = 0
    for i in range(0, len(line)-1, 1):
        if line[i].isdigit():
            total += 10 * int(line[i])
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            total += int(line[i])
            return total
    return total


nums_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def parseForward(line):
    current_string = ''
    for i in range(0, len(line)-1):
        total = 0
        if line[i].isdigit():
            total += 10 * int(line[i])
            return total
        else:
            current_string = current_string + line[i]
            if len(current_string) >= 0:
                for num in nums_map:
                    if current_string.find(num) != -1:
                        total += 10 * nums_map[num]
                        return total


def parseBackward(line):
    current_string = ''
    total = 0
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            total += int(line[i])
            return total
        else:
            current_string = line[i] + current_string
            if len(current_string) >= 0:
                for num in nums_map:
                    if current_string.find(num) != -1:
                        total += nums_map[num]
                        return total


if __name__ == "__main__":
    grand_total = 0
    for line in lines:
        # grand_total += parseLine(line)
        grand_total += parseForward(line)
        grand_total += parseBackward(line)

    print(grand_total)
