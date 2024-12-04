import sys
import re

memory = ''

with open(sys.argv[1]) as f:
    for line in f.readlines():
        memory += line

def extract_number_pairs(input_row):
    pairs = []
    # pattern_part_1 = r"mul\((\d{1,3},\d{1,3})\)"
    pattern_part_2 = r"(mul\((\d{1,3},\d{1,3})\))|(do\(\))|(don't\(\))"
    matches = re.finditer(pattern_part_2, input_row)

    doing = True
    for match in matches: # update this to handle do's and don't's
        text = match.group(0)

        if text == "don't()":
            doing = False
            continue

        if text == "do()":
            doing = True
            continue

        if doing == True:
            pairs.append([int(i) for i in match.group(2).split(',')])

    return pairs

sum = 0
line_pairs = []
line_pairs.extend(extract_number_pairs(memory))

for pair in line_pairs:
    sum += pair[0] * pair[1]

print(f"Sum: {sum}")

