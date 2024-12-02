# python 1.py input.txt
import cmath
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

'''
Time:      7  15   30
Distance:  9  40  200

This document describes three races:

    The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
    The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
    The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.

starting speed = 0 mm / ms

speed increases during button hold at 1 mm / ms

for a given min time, what is the max distance we can get with our constraints

no friction
'''

def extract(lines):
    game_times = re.findall(r'\d+', lines[0])
    game_times = [int(time) for time in game_times]
    game_distances = re.findall(r'\d+', lines[1])
    game_distances = [int(time) for time in game_distances]

    return game_times, game_distances

def extract2(lines):
    game_time = ''
    for l in lines[0]:
        if l.isdigit():
            game_time += l
    game_time = int(game_time)
    game_distance = ''
    for l in lines[1]:
        if l.isdigit():
            game_distance += l
    game_distance = int(game_distance)

    return [game_time], [game_distance]


def solve_quadratic(b, c):
    # Coefficients a, b, c in the equation ax^2 + bx + c = 0
    a = 1

    # Calculating the discriminant
    discriminant = cmath.sqrt(b**2 - 4 * a * c)

    # Two solutions
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)

    return x1, x2

# Example: solve for b = 5, c = 6
solve_quadratic(5, 6)


if __name__ == "__main__":
    # game_times, game_distances = extract(lines)
    game_times, game_distances = extract2(lines)

    margin_counts = []

    for i in range(len(game_times)):
        x1, x2 = solve_quadratic(game_times[i], game_distances[i])
        x1 = math.floor(abs(x1.real))
        x2 = math.ceil(abs(x2.real)-1)

        margin_counts.append(x2 - x1)

    margins_product = math.prod(margin_counts)
    print(margins_product)
