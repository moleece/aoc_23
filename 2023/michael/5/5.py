import sys

def loadInput(fname):
    ''' Return ([seeds], [(maps)])
    '''
    with open(fname, 'r') as f:
        lines = f.readlines()
    seeds = [int(x) for x in lines[0].split(':')[1].strip().split()]
    
    maps = []
    curMap = []
    for line in lines[2:]:
        if len(line) == 1:
            maps += [curMap]
            curMap = []
        elif line[0].isalpha():
            continue
        else:
            curMap += [tuple([int(x) for x in line.split()])]
    maps += [curMap]
    return (seeds, maps)

# Part 1
def traceSeed(seed, maps):
    curIndex = seed
    for map in maps:
        for (destStart, sourceStart, length) in map:
            if curIndex >= sourceStart and curIndex < sourceStart + length:
                curIndex = destStart + (curIndex - sourceStart)
                break
    return curIndex

# Part 2
def preprocess_maps(maps):
    # Fill in gaps with identity matching in case there's gaps.
    newMaps = []
    for mapping in maps:
        m = sorted(mapping, key=lambda x: x[1])
        if m[0][1] != 0:
            m = [(0,0,m[0][1])] + m
        newM = []
        for i in range(len(m)-1):
            newM += [m[i]]
            if m[i][1] + m[i][2] < m[i+1][1]:
                start = m[i][1] + m[i][2]
                newM += [(start, start,  m[i+1][1] - start)]
        newM += [m[-1]]
        endingPoint = m[-1][1] + m[-1][2]
        newM += [(endingPoint, endingPoint, 100000000)]
        newMaps += [newM]
    return newMaps


def traceSeed_ranges(seed, length, maps):
    maps = preprocess_maps(maps)
    ranges = [(seed, length)]
    for map in maps:
        newRanges = []
        for (rangeStart, rangeLength) in ranges:
            for (destStart, sourceStart, mapLength) in map:
                i_start, i_len = intersect(sourceStart, mapLength, rangeStart, rangeLength)
                if i_len > 0:
                    newRanges += [(destStart + (i_start - sourceStart), i_len)]
        ranges = newRanges
    return ranges

def intersect(xStart, xLen, yStart, yLen):
    if xStart > yStart:
        if yStart + yLen < xStart:
            return (-1, 0)
        return (xStart, min(xStart+xLen, yStart+yLen)-xStart)
    else:
        if xStart + xLen < yStart:
            return (-1, 0)
        return (yStart, min(yStart+yLen, xStart+xLen)-yStart)


if __name__ == '__main__':
    (seeds, maps) = loadInput('./michael/5/data')
    all_ranges = traceSeed_ranges(seeds[0], seeds[1], maps)
    for i in range(2, len(seeds), 2):
        all_ranges += traceSeed_ranges(seeds[i], seeds[i+1], maps)
    print(min([x[0] for x in all_ranges]))