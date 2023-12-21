import sys

class FlipFlop:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets
        self.on = False

    def handlePulse(self, pulsingModule, isHigh):
        sendPulses = []
        if not isHigh:
            toSend = not self.on
            self.on = not self.on
            for t in self.targets:
                sendPulses += [(self, t, toSend)]
        return sendPulses

class Conjunction:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets
        self.inputs = {}

    def handlePulse(self, pulsingModule, isHigh):
        self.inputs[pulsingModule.name] = isHigh
        toSend = not (sum(self.inputs.values()) == len(self.inputs))
        sendPulses = []
        for t in self.targets:
            sendPulses += [(self, t, toSend)]
        return sendPulses

class Broadcaster:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets

    def handlePulse(self, pulsingModule, isHigh):
        return [(self, t, isHigh) for t in self.targets]

class Sink:
    def __init__(self, name):
        self.name = name
        self.targets = []
    
    def handlePulse(self, pulsingModule, isHigh):
        return []


def preprocess(modules):
    # {name: module}
    sinks = {}
    for m in modules:
        for t in modules[m].targets:
            if t not in modules:
                s = Sink(t)
                sinks[t] = s
    for s in sinks:
        modules[s] = sinks[s]

    for m in modules:
        modules[m].targets = [modules[t] for t in modules[m].targets]
        for t in modules[m].targets:
            if isinstance(t, Conjunction):
                t.inputs[m] = False
    
    return modules

def buildModule(line):
    (name, targets) = line.split(' -> ')
    kind = name[0]
    name = name[1:]
    targetNames = targets.split(', ')
    if kind == '%':
        return FlipFlop(name, targetNames)
    elif kind == '&':
        return Conjunction(name, targetNames)
    else:
        return Broadcaster(name, targetNames)
    return None


accumFeeders = set(['kz', 'qs', 'xj', 'km'])

def pushButton(modules):
    pulses = [(modules['roadcaster'], modules['roadcaster'], False)]
    lowPulses = 0
    highPulses = 0
    rxLowPulse = False
    feederPulses = {x:[] for x in accumFeeders}
    while len(pulses) > 0:
        (fromModule, toModule, isHigh) = pulses.pop(0)
        if toModule.name == 'rx' and not isHigh:
            rxLowPulse = True
        if fromModule.name in feederPulses and toModule.name == 'gq':
            feederPulses[fromModule.name] += [isHigh]
        # print(fromModule.name, isHigh, toModule.name)
        highPulses += isHigh
        lowPulses += not isHigh
        pulses += toModule.handlePulse(fromModule, isHigh)
    return (lowPulses, highPulses, rxLowPulse, feederPulses)

        

if __name__ == '__main__':
    with open('michael/20/data') as f:
        lines = f.readlines()

    modules = {}
    for line in lines:
        m = buildModule(line.strip())
        modules[m.name] = m 
    
    modules = preprocess(modules)

    lows, highs, rxLowPulse = 0,0,False
    i = 0
    fPulses = []
    while not rxLowPulse:
        if (i+1) % 100000 == 0:
            break
        (low, high, rxLowPulse, feederPulses) = pushButton(modules)
        lows += low
        highs += high
        i += 1
        fPulses += [feederPulses]

    # Ran in debug console:
    # km = [True in fPulses[i]['km'] for i in range(len(fPulses))]
    # km_indices = [i for i in range(len(km)) if km[i]]
    # [km_indices[i+1] - km_indices[i] for i in range(len(km_indices)-1)]
    # -> [4093, 4093, 4093, 4093, 4093, 4093...

    # Repeating for the other nodes that feed into the rx accumulator gave 4093, 3911, 4019, and 3733
    # Multiplying those together gave the answer (didn't check, but they must be relative primes)

    # I'm not convinced this is true for any arbitrary input, or whether they just set it up
    # to have uniform cycle lengths nicely for us.

    print(lows, highs)
    print(i)


