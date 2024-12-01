import sys

# P1
def expandGalaxies(lines):
    newLines = []
    doubleCols = set(range(len(lines[0])))
    for line in lines:
        if line == '.' * len(line):
            newLines += [line] * 2
        else:
            newLines += [line]
        for j in range(len(line)):
            if line[j] == '#':
                doubleCols.discard(j)
    doubleCols = sorted(list(doubleCols), reverse=True)
    for i in range(len(newLines)):
        for j in doubleCols:
            newLines[i] = newLines[i][:j] + '.' + newLines[i][j:]
    return newLines

def pairDistances(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                galaxies += [(i,j)]
    
    dists = []
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            dists += [(abs(galaxies[i][0] - galaxies[j][0]) + 
                       abs(galaxies[i][1] - galaxies[j][1]))]
    
    return dists

# P2
def expandedRows(lines):
    rs = []
    for i in range(len(lines)):
        if lines[i] == '.' * len(lines[i]):
            rs += [i]
    return set(rs)

def expandedCols(lines):
    cs = set(range(len(lines[0])))
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == '#':
                cs.discard(j)
                break
    return cs

def pairDistances_p2(lines):
    rs = expandedRows(lines)
    cs = expandedCols(lines)

    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                galaxies += [(i,j)]
    
    dists = []
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            dists += [dist(galaxies[i], galaxies[j], rs, cs)]
    
    return dists

def dist(g1, g2, rs, cs):
    # Binary search and ranges would scale better, but this is fine for input size
    expandedRows = 0
    for i in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
        if i in rs:
            expandedRows += 1
    expandedCols = 0
    for i in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
        if i in cs:
            expandedCols += 1
    
    multiplier = 1000000
    return (abs(g1[0]-g2[0]) + abs(g1[1] - g2[1]) + (multiplier-1) * (expandedRows + expandedCols))
    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    dists = pairDistances_p2(lines)
    print(sum(dists))