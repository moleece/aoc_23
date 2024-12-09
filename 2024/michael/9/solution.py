import sys

with open(sys.argv[1]) as f:
    line = list(f.readline().strip())

disk = []
diskId = 0
for i in range(len(line)):
    if i % 2 == 0:
        disk += [diskId] * int(line[i])
        diskId += 1
    else:
        disk += ['.'] * int(line[i])

# Part 1
def compress_disk(disk):
    compressed_disk = []
    left_counter = 0
    right_counter = len(disk) - 1
    while right_counter >= left_counter:
        if disk[left_counter] != '.':
            compressed_disk += [disk[left_counter]]
            left_counter += 1
            continue
        if disk[right_counter] == '.':
            right_counter -= 1
            continue
        compressed_disk += [disk[right_counter]]
        right_counter -= 1
        left_counter += 1
    return compressed_disk



def checksum(disk):
    return sum([i*int(disk[i]) for i in range(len(disk))])


# Part 2
def compress_disk_blocks(line):
    # blocks = {id: (len, startPos)}
    # gaps = [(len, startPos)]
    blocks = {}
    gaps = []
    startPos = 0
    for i in range(len(line)):
        if i % 2 == 0:
            blocks[i//2] =(int(line[i]), startPos)
            startPos += int(line[i])
        else:
            gaps += [(int(line[i]), startPos)]
            startPos += int(line[i])
    
    for blockId in sorted(blocks.keys(), reverse=True):
        blockLen, startPos = blocks[blockId]

        for j in range(len(gaps)):
            gapLen, gapStartPos = gaps[j]
            if gapStartPos > startPos:
                break
            if gapLen >= blockLen:
                blocks[blockId] = (blockLen, gapStartPos)
                gaps[j] = (gapLen - blockLen, gapStartPos + blockLen)
                break

    return blocks

def checksum_blocks(blocks):
    total = 0
    for blockId in blocks:
        blockLen, startPos = blocks[blockId]
        for i in range(startPos, startPos+blockLen):
            total += blockId * i
    return total

print(checksum_blocks(compress_disk_blocks(line)))

