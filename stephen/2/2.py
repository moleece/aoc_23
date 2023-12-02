# python 1.py input.txt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

color_maximums = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parseLine(line):
    gameId = int(line.split(': ')[0].split(' ')[1])
    game_sets = line.split(': ')[1].split('; ')
    for set in game_sets:
        color_counts = set.split(', ')
        for count in color_counts:
            count = count.strip()
            if int(count.split(' ')[0]) > color_maximums[count.split(' ')[1]]:
                return 0

    return gameId


def parseLine2(line):
    color_pulls = {
        'blue': [],
        'green': [],
        'red': []
    }

    all_pulls = line.split(': ')[1].replace(';', ',').split(', ')
    for pull in all_pulls:
        color_pulls[pull.split(' ')[1].strip()].append(int(pull.split(' ')[0].strip()))
    
    power = max(color_pulls['blue']) *max(color_pulls['green']) * max(color_pulls['red']) 

    return power


if __name__ == "__main__":
    # total = 0
    # for line in lines:
    #     total += parseLine(line)
    # print(total)

    power_sum = 0
    for line in lines:
        power_sum += parseLine2(line)
    print(power_sum)

