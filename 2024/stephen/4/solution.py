"""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


from typing import List, Dict, Optional
import sys
import re

lines = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        lines.append(line.strip())

horizontals: Dict[int,str] = {}
verticals: Dict[int,str] = {}
diagonals_down: Dict[int,str] = {}
diagonals_up: Dict[int,str] = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if horizontals.get(y, ''):
            horizontals[y] += char
        else:
            horizontals[y] = char
        if verticals.get(x, ''):
            verticals[x] += char
        else:
            verticals[x] = char
        if diagonals_down.get(x-y, ''):
            diagonals_down[x-y] += char
        else:
            diagonals_down[x-y] = char
        if diagonals_up.get(y+x, ''): # fix
            diagonals_up[y+x] += char
        else:
            diagonals_up[y+x] = char

count = 0
pattern = r"(XMAS)"
for lines_hash in [horizontals, verticals, diagonals_up, diagonals_down]:
    for line in lines_hash.values():
        line_reversed = line[::-1]
        count += len(re.findall(pattern, line))
        count += len(re.findall(pattern, line_reversed))


rows = len(lines)
cols = len(lines[0])
valid_diagonals = [("M", "A", "S"), ("S", "A", "M")]
mas_count = 0

for y in range(1, rows-1):
    for x in range(1, cols-1):
        center = lines[y][x]
        if center != 'A':
            continue
        
        diagonal1 = (lines[y-1][x-1])
        diagonal1 = (lines[y-1][x-1], lines[y][x], lines[y+1][x+1])
        diagonal2 = (lines[y-1][x+1], lines[y][x], lines[y+1][x-1])

        if diagonal1 in valid_diagonals and diagonal2 in valid_diagonals:
            mas_count += 1

print(f"MAS count: {mas_count}")






