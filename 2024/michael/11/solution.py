import sys, copy



def blink(stones):
    new_stones = []
    for s in stones:
        if s == '0':
            new_stones.append('1')
        elif len(s) % 2 == 0:
            new_stones.append(s[:len(s)//2])
            new_stones.append(str(int(s[len(s)//2:])))
        else:
            new_stones.append(str(int(s)*2024))
    return new_stones

def get_stone_list(stones):
    tmp = copy.deepcopy(stones)
    allStonesSeen = set(stones)
    oldSeen = 0
    while oldSeen != len(allStonesSeen):
        tmp = blink(tmp)
        tmp = [s for s in tmp if s not in allStonesSeen]
        oldSeen = len(allStonesSeen)
        allStonesSeen.update(tmp)
    return allStonesSeen

if __name__ == '__main__':
    with(open(sys.argv[1], 'r')) as f:
        stones = f.readline().strip().split()

    all_stones = list(get_stone_list(stones))

    grid = [{s:1 for s in all_stones} for _ in range(76)]
    for i in range(1, 76):
        for j in all_stones:
            decomposition = blink([j])
            grid[i][j] = 0
            for d in decomposition:
                grid[i][j] += grid[i-1][d]
    
    print(sum([grid[75][s] for s in stones]))
    
