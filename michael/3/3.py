'''
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''


import sys, math

# P1
def checkNum(adj, num, ni, nj):
    width = math.ceil(math.log10(num+0.1))
    for i in range(ni-1, ni + 2):
        for j in range(nj-1, nj + width + 1):
            if i < 0 or i >= len(adj):
                continue
            if j < 0 or j >= len(adj[i]):
                continue
            if adj[i][j].isalnum() or adj[i][j] == '.':
                continue
            return True

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    adj = [[c for c in line.strip()] for line in lines]
    total = 0
    for i in range(len(adj)):
        j = 0
        while j < len(adj[i]):
            if adj[i][j].isdigit():
                part = int(adj[i][j])
                j += 1
                while j < len(adj[i]) and adj[i][j].isdigit():
                    part = part*10 + int(adj[i][j])
                    j += 1
                if checkNum(adj, part, i, j-math.ceil(math.log10(part+0.1))):
                    total += part
            else:
                j += 1
    print(total)
