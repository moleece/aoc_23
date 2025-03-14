import sys


class Gate:

    def __init__(self, x1, x2, op, name):
        self.x1 = x1
        self.x2 = x2
        self.op = op
        self.value = None
        self.name = name
    
    def simulate(self):
        if self.x2 is None:
            return self.x1
        elif self.value is not None:
            return self.value
        elif self.op == 'AND':
            self.value = self.x1.simulate() & self.x2.simulate()
        elif self.op == 'OR':
            self.value = self.x1.simulate() | self.x2.simulate()
        elif self.op == 'XOR':
            self.value = self.x1.simulate() ^ self.x2.simulate()


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]

    gates = {}
    # Build the inputs
    while ': ' in lines[0]:
        line = lines.pop(0)
        name, value = line.split(': ')
        value = int(value)
        gates[name] = (Gate(value, None, None, name))

    _ = lines.pop(0)
    
    newLines = []
    for line in lines:
        s = line.split(' ')
        ks = set([s[0], s[2]])
        op = s[1]
        name = s[4]
        newLines.append([len(ks.intersection(gates.keys())), ks, op, name])
    newLines = sorted(newLines, reverse=True)

    while len(newLines) > 0:
        if newLines[0][0] != 2:
            for i in range(len(newLines)):
                line = newLines[i]
                newLines[i][0] = len(line[1].intersection(gates.keys()))
            newLines = sorted(newLines, reverse=True)
        else:
            line = newLines.pop(0)
            ks, op, name = line[1], line[2], line[3]
            x1 = ks.pop()
            x2 = ks.pop()
            gates[name] = (Gate(gates[x1], gates.get(x2), op, name))
    
    for g in gates:
        gates[g].simulate()
    
    zs = []
    for g in gates:
        if g[0] == 'z':
            zs.append((g, gates[g].value))
    zs = sorted(zs, key=lambda x: x[0], reverse=True)

    nStr = ''.join([str(z[1]) for z in zs])
    print(nStr)
    print(int(nStr, 2))


    