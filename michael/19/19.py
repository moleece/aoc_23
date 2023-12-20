import sys, operator
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
    def __init__(self, attr, function, comparator, target, workflowName, number, rangesToReach):
        self.name = workflowName + '.' + str(number)
        if workflowName != 'A' and workflowName != 'R':
            self.attr = attr
            self.function = function
            self.comparator = comparator
            self.leftChild = target + '.0'
            self.rightChild = workflowName + '.' + str(number+1)
        self.rangesToReach = rangesToReach # {'a': (min, max)}
    
    def countChildren(self, side):
        newRanges = self.rangesToReach
        if (self.function == operator.gt and side == 'left' or
            self.function == operator.lt and side == 'right'):
            newRanges[self.attr][0] = max(newRanges[self.attr][0], self.comparator+1)
        else:
            newRanges[self.attr][1] = min(newRanges[self.attr][1], self.comparator-1)
        accum = 1
        for r in newRanges:
            if newRanges[r][1] < newRanges[r][0]:
                return 0
            accum *= newRanges[r][1] - newRanges[r][0] + 1
        return accum
    

    def applyConstraint(self, attr, function, comparator, side):
        if (function == operator.gt and side == 'left' or
            function == operator.lt and side == 'right'):
            self.rangesToReach[attr][0] = max(self.rangesToReach[attr][0], comparator+1)
        else:
            self.rangesToReach[attr][1] = min(self.rangesToReach[attr][1], comparator-1)

    

if __name__ == '__main__':
    with open('michael/19/ex') as f:
    # with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    
    nodes = {'A.0': 'A', 'R.0': 'R'}
    i = 0
    while lines[i] != '':
        w = Workflow(lines[i])
        for j in range(len(w.rules)):
            rule = w.rules[j]
            n = Node(rule.attr, rule.f, rule.v, rule.dest, w.name, j, {'x':[0,4000], 'm':[0,4000], 'a':([0,4000]), 's':([0,4000])})
            nodes[n.name] = n
        fallbackNode = Node('a', operator.gt, -1, w.fallback, w.name, j+1, {'x':([0,4000]), 'm':([0,4000]), 'a':([0,4000]), 's':([0,4000])})
        nodes[fallbackNode.name] = fallbackNode
        i += 1
    print(nodes)
    
    for node in nodes:
        if node == 'A.0' or node == 'R.0':
            continue
        print(node, nodes[node].leftChild, nodes[node].rightChild)
        nodes[node].leftChild = nodes[nodes[node].leftChild]
        try:
            nodes[node].rightChild = nodes[nodes[node].rightChild]
        except:
            continue
    
    toUpdate = ['in.0']
    total = 0
    while len(toUpdate) > 0:
        nextUpdate = toUpdate.pop()
        node = nodes[nextUpdate]
        if node.leftChild == 'A':
            total += node.countChildren('left')
        elif node.leftChild != 'R':
            try:
                for a in node.rangesToReach:
                    node.leftChild.rangesToReach[a] = deepcopy(node.rangesToReach[a])
                node.leftChild.applyConstraint(node.attr, node.function, node.comparator, 'left')
                toUpdate += [node.leftChild.name]
            except:
                continue
        if node.rightChild == 'A.0':
            total += node.countChildren('right')
        elif node.rightChild != 'R.0':
            try:
                for a in node.rangesToReach:
                    node.rightChild.rangesToReach[a] = deepcopy(node.rangesToReach[a])
                node.rightChild.applyConstraint(node.attr, node.function, node.comparator, 'right')
                toUpdate += [node.rightChild.name]
            except:
                continue

    for n in nodes:
        try:
            print(n, nodes[n].rangesToReach)
        except:
            print(n)
    
    print(total)