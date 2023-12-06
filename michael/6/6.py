'''
z = x*(t-x)
0 = x^2 - tx + z

(t +- sqrt(t^2 - 4z)) / 2
t = 7
z = 9

(7 + sqrt(49 - 36)) / 2
(7 +- 3.6) / 2
1.7, 5.3
'''
import math, sys

def parseFile(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    times = [int(x) for x in lines[0].split(':')[1].split()]
    dists = [int(x) for x in lines[1].split(':')[1].split()]
    return [(times[i], dists[i]) for i in range(len(times))]

def parseFile_2(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    times = [int(lines[0].split(':')[1].replace(' ', ''))]
    dists = [int(lines[1].split(':')[1].replace(' ', ''))]
    return [(times[i], dists[i]) for i in range(len(times))]

if __name__ == '__main__':
    tdPairs = parseFile_2(sys.argv[1])
    counts = []
    for (time, distance) in tdPairs:
        minTime = (time - math.sqrt(time**2 - 4*distance)) / 2
        maxTime = (time + math.sqrt(time**2 - 4*distance)) / 2
        counts += [math.floor(maxTime-0.001) - math.ceil(minTime+0.001) + 1]
    print(counts)
    print(math.prod(counts))




