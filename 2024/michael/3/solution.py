import sys, re

with open(sys.argv[1]) as f:
    line = f.read()

## P1
total = 0
for m in re.finditer('mul\(\d{1,3},\d{1,3}\)', line):
    a, b = map(int, m.group().split('(')[1].split(')')[0].split(','))
    total += a * b

print(total)

## P2
total = 0
active = True
for m in re.finditer('(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', line):
    if m.group() == 'do()':
        active = True
    elif m.group() == 'don\'t()':
        active = False
    elif active:
        a, b = map(int, m.group().split('(')[1].split(')')[0].split(','))
        total += a * b

print(total)

