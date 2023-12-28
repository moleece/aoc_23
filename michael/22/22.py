import sys

class Block:
    def __init__(self, line):
        self.line = line
        (x,y,z) = line.split('~')[0].split(',')
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        (x2, y2, z2) = line.split('~')[1].split(',')
        self.dx = int(x2)-self.x
        self.dy = int(y2)-self.y 
        self.dz = int(z2)-self.z
        self.supporting = []
        self.supportedBy = []


def dropBlocks(blocks):
    blocks = sorted(blocks, key=lambda x: x.z)
    width = max([b.x for b in blocks]) + 1
    height = max([b.y for b in blocks]) + 1
    heightGrid = [[(1,None)]*width for _ in range(height)]

    # print(width, height)
    for b in blocks:
        # print()
        # for l in heightGrid:
        #     print([x[0] for x in l])
        # print(b.line)
        # print(b.dx, b.dy)

        maxHeight = 0
        supportedBy = []
        # Find settling height and blocks supporting you
        for i in range(max([b.dx, b.dy])+1):
            if heightGrid[b.y + i*(b.dy!=0)][b.x + i*(b.dx!=0)][0] > maxHeight:
                maxHeight = heightGrid[b.y + i*(b.dy!=0)][b.x + i*(b.dx!=0)][0]
                supportedBy = [heightGrid[b.y + i*(b.dy!=0)][b.x + i*(b.dx!=0)][1]]
            elif heightGrid[b.y + i*(b.dy!=0)][b.x + i*(b.dx!=0)][0] == maxHeight:
                supportedBy += [heightGrid[b.y + i*(b.dy!=0)][b.x + i*(b.dx!=0)][1]]
        
        # Update the maxHeight grid
        # print(maxHeight)
        for i in range(max([b.dx, b.dy])+1):
            # print('updating', b.y + i*(b.dy!=0), b.x + (b.dx!=0))

            heightGrid[b.y + i*(b.dy!=0)][b.x + i*(b.dx!=0)] = (maxHeight + b.dz + 1, b)

        # Add yourself to supporting lists
        supportedBy = list(set(list(filter(lambda x: x, supportedBy))))
        for s in supportedBy:
            s.supporting += [b]

        # Set your own supportedBy
        b.supportedBy = supportedBy

    return (heightGrid, blocks)




if __name__ == '__main__':
    # with open('michael/22/ex') as f:
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

    blocks = [Block(line) for line in lines]
    (heightGrid, blocks) = dropBlocks(blocks)

    for l in heightGrid:
        print([x[0] for x in l])

    # P1
    total = 0
    for b in blocks:
        soloSupport = False
        for top in b.supporting:
            if len(top.supportedBy) <= 1:
                soloSupport = True
                break
        if not soloSupport:
            total += 1
    print(total)

    # P2
    fallingNums = []
    for b in blocks:
        fallingSet = set([b])
        toProcess = [b]
        while toProcess:
            b2 = toProcess.pop(0)
            for b3 in b2.supporting:
                if len(set(b3.supportedBy).intersection(fallingSet)) == len(b3.supportedBy):
                    fallingSet.add(b3)
                    toProcess += [b3]
        fallingNums += [(len(fallingSet)-1)]
    print(sum(fallingNums))
