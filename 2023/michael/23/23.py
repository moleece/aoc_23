import sys, itertools

class Node:
    nextId = itertools.count()

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.id = next(Node.nextId)
        self.adjacencyList = []
    
    def __hash__(self):
        return hash((self.i, self.j))
    
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

def buildGraph(lines):
    nodes = set([Node(0,1)])
    nextNode = walkPath(0,1,'n',lines)
    print(nextNode)


dirMap = {'s':(1,0),'n':(-1,0),'w':(0,-1),'e':(0,1)}
invMap = {'s':'n','n':'s','e':'w','w':'e'}
def walkPath(i, j, fromDir, lines):
    nextSteps = []
    for d in dirMap:
        if d == fromDir:
            continue
        (di, dj) = dirMap[d]
        ni, nj = i+di,j+dj
        if ni<0 or ni > len(lines) or nj<0 or nj>len(lines):
            continue
        if lines[ni][nj] not in ['.', '>', '<', 'v', '^']:
            continue
        nextSteps += [(ni, nj, d)]
    
    thisOneWay = lines[i][j] in ['>', '<', 'v', '^']
    if len(nextSteps) > 1:
        return (0, Node(i,j), False)
    elif len(nextSteps) == 1:
        (ni, nj, direction) = nextSteps[0]
        (dist, destNode, oneWay) = walkPath(ni, nj, invMap[direction], lines)
        return (1+dist, destNode, oneWay or thisOneWay)

    # Hit a branching point
    if len(paths) > 1:
        return (i, j, 0, False)

    (destI, destJ, d, oneWay) = list(paths.values())[0]
    if lines[i][j] == '.':
        return (destI, destJ, d+1, oneWay)
    else:
        return (destI, destJ, d+1, True)

        
    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    
    graph = buildGraph(lines)