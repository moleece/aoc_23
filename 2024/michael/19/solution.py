import sys

def can_make(towels, pattern):
    i = 0
    possible = [0] * (len(pattern)+1)
    possible[-1] = 1
    for i in range(len(pattern)-1, -1, -1):
        for towel in towels:
            if towel == pattern[i:i+len(towel)] and (possible[i+len(towel)] or i+len(towel) == len(pattern)):
                possible[i] += possible[i+len(towel)]
    return possible[0]

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        towels = f.readline().strip().split(', ')
        f.readline()
        patterns = [line.strip() for line in f.readlines()]
    
    total = 0
    for pattern in patterns:
        total += can_make(towels, pattern)
    print(total)
