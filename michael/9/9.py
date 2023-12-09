import sys

def nextNum(sequence):
    sequences = [sequence]
    while sequences[-1][0] != 0 or sum(sequences[-1]) != 0:
        newSequence = []
        for i in range(len(sequences[-1])-1):
            newSequence += [sequences[-1][i+1] - sequences[-1][i]]
        sequences += [newSequence]
    
    # Work up to front
    for i in range(len(sequences)-1, 0, -1):
        sequences[i-1] += [sequences[i-1][-1] + sequences[i][-1]]
    
    return sequences[0][-1]

def prevNum(sequence):
    sequences = [sequence]
    while sequences[-1][0] != 0 or sum(sequences[-1]) != 0:
        newSequence = []
        for i in range(len(sequences[-1])-1):
            newSequence += [sequences[-1][i+1] - sequences[-1][i]]
        sequences += [newSequence]
    
    # Work up to front
    for i in range(len(sequences)-1, 0, -1):
        sequences[i-1] = [sequences[i-1][0] - sequences[i][0]] + sequences[i-1]
    
    return sequences[0][0]

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    nextNums = []
    for line in lines:
        sequence = [int(x) for x in line.split()]
        nextNums += [prevNum(sequence)]
    print(nextNums)
    print(sum(nextNums))

    