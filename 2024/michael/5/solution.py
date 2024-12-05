import sys
from collections import defaultdict

followers = defaultdict(list)
sequences = []
with open(sys.argv[1]) as f:
    line = f.readline().strip()
    while line:
        first, second = line.split("|")
        followers[first].append(second)
        line = f.readline().strip()
    for line in f.readlines():
        sequences.append(line.strip().split(','))

## P1

def sequence_value(sequence):
    for i in range(len(sequence) - 1):
        for j in range(i, len(sequence)):
            if sequence[i] in followers[sequence[j]]:
                return 0
    return int(sequence[len(sequence)//2])

total = 0
for sequence in sequences:
    total += sequence_value(sequence)
print(total)                


## P2
bad_sequences = [s for s in sequences if sequence_value(s) == 0]
def reorder_sequence(sequence):
    for i in range(len(sequence) - 1):
        for j in range(i, len(sequence)):
            if sequence[i] in followers[sequence[j]]:
                sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence

reordered_sequences = [reorder_sequence(s) for s in bad_sequences]
total = 0
for s in reordered_sequences:
    total += int(s[len(s)//2])
print(total)