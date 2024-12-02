import sys
from collections import defaultdict

l1 = []
l2 = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        s = line.split()
        l1.append(int(s[0]))
        l2.append(int(s[1]))

l1 = sorted(l1)
l2 = sorted(l2)

## P1
total = 0
for i in range(len(l1)):
    total += abs(l1[i] - l2[i])

print("P1:", total)

## P2
nCounts = defaultdict(int)
similarityScore = 0
for i in range(len(l2)):
    nCounts[l2[i]] += 1

for i in range(len(l1)):
    similarityScore += l1[i] * nCounts[l1[i]]

print("P2:", similarityScore)
    