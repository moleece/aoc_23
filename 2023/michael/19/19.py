import sys, operator, math
from copy import deepcopy

# P1
class Workflow:

    def __init__(self, line):
        self.name = line.split('{')[0]
        rules = line.split('{')[1][:-1].split(',')
        self.fallback = rules[-1]
        self.rules = [Rule(r) for r in rules[:-1]]
    
    def processPart(self, part):
        for rule in self.rules:
            dest = rule.processPart(part)
            if dest:
                return dest
        return self.fallback

condMap = {'<': operator.lt, '>': operator.gt}

class Rule:
    def __init__(self, rString):
        self.attr = rString[0]
        self.f = condMap[rString[1]]
        self.v = int(rString[2:].split(':')[0])
        self.dest = rString.split(':')[-1]
    
    def processPart(self, part):
        x = part.get(self.attr)
        if self.f(x, self.v):
            return self.dest
        else:
            return None

class Part:
    def __init__(self, line):
        self.attrs = {}
        for a in line[1:-1].split(','):
            (name, v) = a.split('=')
            self.attrs[name] = int(v)

    def get(self, attrName):
        return self.attrs[attrName]


# if __name__ == '__main__':
#     with open(sys.argv[1]) as f:
#         lines = [line.strip() for line in f.readlines()]
    
#     workflows = {}
#     i = 0
#     while lines[i] != '':
#         w = Workflow(lines[i])
#         workflows[w.name] = w
#         i += 1
    
#     parts = []
#     for j in range(i+1, len(lines)):
#         parts += [Part(lines[j])]

#     accepted = []
#     for p in parts:
#         status = workflows['in'].processPart(p)
#         while status != 'R' and status != 'A':
#             status = workflows[status].processPart(p)
#         if status == 'A':
#             accepted += [p]
    
#     print([p.attrs for p in accepted])
#     total = 0
#     for p in accepted:
#         for a in p.attrs:
#             total += p.attrs[a]
#     print(total)

# P2
class Node:
    def __init__(self, attr, function, comparator, leftChild, rightChild):
        self.name = ''
        self.attr = attr
        self.function = function
        self.comparator = comparator
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getRange(self):
        if self.function == operator.lt:
            return (self.attr, 1, self.comparator-1)
        else:
            return (self.attr, self.comparator+1, 4000)
    
    def getInvertedRange(self):
        if self.function == operator.lt:
            return (self.attr, self.comparator, 4000)
        else:
            return (self.attr, 1, self.comparator)


def buildSubtree(workflows, workflowName, stepIndex):
    if workflowName in ['A', 'R']:
        return Node(workflowName, None, None, None, None)
    
    w = workflows[workflowName]
    
    if stepIndex == len(w.rules):
        return buildSubtree(workflows, w.fallback, 0)
    
    rule = w.rules[stepIndex]
    leftChild = buildSubtree(workflows, rule.dest, 0)
    rightChild = buildSubtree(workflows, workflowName, stepIndex+1)
    n = Node(rule.attr, rule.f, rule.v, leftChild, rightChild)
    n.name = workflowName + '.' + str(stepIndex)
    return n

def countAccepts(treeNode, constraints):
    if treeNode.leftChild == None and treeNode.rightChild == None:
        if treeNode.attr == 'A':
            return countPossibilities(constraints)
        else:
            return 0
    
    return (countAccepts(treeNode.leftChild, constraints + [treeNode.getRange()]) + 
            countAccepts(treeNode.rightChild, constraints + [treeNode.getInvertedRange()]))

def countPossibilities(constraints):
    ranges = {'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}
    for (attr, minVal, maxVal) in constraints:
        ranges[attr][0] = max(minVal, ranges[attr][0])
        ranges[attr][1] = min(maxVal, ranges[attr][1])
    rangeLens = [ranges[x][1] - ranges[x][0] + 1 for x in ranges]
    if min(rangeLens) <= 0:
        return 0
    return math.prod(rangeLens)

if __name__ == '__main__':
    with open('michael/19/data') as f:
    # with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    
    workflows = {}
    i = 0
    while lines[i] != '':
        w = Workflow(lines[i])
        workflows[w.name] = w
        i += 1

    i = 0
    tree = buildSubtree(workflows, 'in', 0)
    
    # Traverse the tree
    print(countAccepts(tree, []))
    