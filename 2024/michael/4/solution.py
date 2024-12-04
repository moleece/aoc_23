import sys

with open(sys.argv[1]) as f:
    lines = [l.strip() for l in f.readlines()]

## P1
total = 0
# Horizontal
for i in range(len(lines)):
    for j in range(len(lines[0]) - 3):
        if lines[i][j:j+4] == 'XMAS' or lines[i][j:j+4] == 'SAMX':
            total += 1

# Vertical
for i in range(len(lines) - 3):
    for j in range(len(lines[0])):
        if lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
            total += 1
        if lines[i][j] == 'S' and lines[i+1][j] == 'A' and lines[i+2][j] == 'M' and lines[i+3][j] == 'X':
            total += 1

# Diagonal falling
for i in range(len(lines) - 3):
    for j in range(len(lines[0]) - 3):
        if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
            total += 1
        if lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M' and lines[i+3][j+3] == 'X':
            total += 1

# Diagonal rising
for i in range(3, len(lines)):
    for j in range(len(lines[0]) - 3):
        if lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
            total += 1
        if lines[i][j] == 'S' and lines[i-1][j+1] == 'A' and lines[i-2][j+2] == 'M' and lines[i-3][j+3] == 'X':
            total += 1

print(total)


## P2
total = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines)-1):
        if lines[i][j] != 'A':
            continue
        upwardsChars = {lines[i+1][j-1], lines[i-1][j+1]}
        downwardsChars = {lines[i-1][j-1], lines[i+1][j+1]}
        if 'M' in upwardsChars and 'S' in upwardsChars and upwardsChars == downwardsChars:
            total += 1

print(total)