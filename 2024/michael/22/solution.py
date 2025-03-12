import sys
from collections import defaultdict

def simulate(seed, length):
    n = seed
    for i in range(length):
        x = n << 6
        n = n ^ x
        n = n & 0xffffff
        x = n >> 5
        n = n ^ x
        n = n & 0xffffff
        x = n << 11
        n = n ^ x
        n = n & 0xffffff
    return n

def simulateSequence(seed, length):
    n = seed
    ns = [n]
    for i in range(length):
        x = n << 6
        n = n ^ x
        n = n & 0xffffff
        x = n >> 5
        n = n ^ x
        n = n & 0xffffff
        x = n << 11
        n = n ^ x
        n = n & 0xffffff
        ns.append(n % 10)
    return ns


def p2(seeds):
    totals = defaultdict(int)
    for seed in seeds:
        ns = simulateSequence(seed, 2000)
        d = {}
        for i in range(2000, 4, -1):
            seq = (ns[i-3]-ns[i-4], ns[i-2]-ns[i-3], ns[i-1]-ns[i-2], ns[i]-ns[i-1])
            d[seq] = ns[i]
        for k in d:
            totals[k] += d[k]
    
    maxTotal = max(totals.values())
    for k in totals:
        if totals[k] == maxTotal:
            print(k, totals[k])
    return maxTotal
        


            




if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        seeds = [int(line.strip()) for line in f]

    # for seed in seeds:
    #     print(seed, simulate(seed, 2000))
    
    # print(sum([simulate(seed, 2000) for seed in seeds]))

    print(p2(seeds))