import sys



if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    
    start = (-1,-1)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                start = (i,j)
    
    # P1
    curLocations = set([(130,65),(65,130)])
    newLocations = set()
    numSteps = 130
    for _ in range(numSteps):
        for (i, j) in curLocations:
            for (di, dj) in [(0,1),(0,-1),(-1,0),(1,0)]:
                if i+di < 0 or i + di >= len(lines) or j + dj < 0 or j + dj >= len(lines[0]):
                    continue
                elif lines[i+di][j+dj] == '#':
                    continue
                else:
                    newLocations.add((i+di, j+dj))
        curLocations = newLocations
        newLocations = set()

    # P2
    # print(start, len(lines), len(lines[0]))
    # (65, 65) 131 131
    # 128 steps to each corner, clear paths to all

    # Count the number of reachable points per grid with odd # steps using P1 code
    # 7717

    # Count the number of reachable points per grid with even # steps using P1 code
    # 7693

    # 26501365 / 131 ~= 202300.5

    # Count reachable in 130 steps from:
    # left         5844
    # top          5816
    # right        5789
    # bottom       5817
    # *1 these


    # 130
    # left,bottom  6785
    # right,bottom 6749
    # left,top     6776
    # right,top    6757

    # *202299 these

    # Count reachable in 64 steps from:
    # lower left   980
    # lower right  981
    # upper left   980
    # upper right  970
    # *202300 these

    # Number of full even squares:
    # 202300**2

    # Number of full odd squares:
    # 202299**2

    # Total
    # 5844 + 5816 + 5789 + 5817 + 
    # (6785 + 6749 + 6776 + 6757) * 202299 + 
    # (980 + 981 + 980 + 970) * 202300 + 
    # 202299**2 * 7717 + 202300**2 * 7693
    # = 630661863455116

    print(len(curLocations))