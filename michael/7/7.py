import sys

def handType(hand):
    bestHand = '1'
    for l in hand:
        # Part 2, jokers
        h = hand.replace('J', l)
        h = ''.join(sorted(h))
        val = '1'
        if h == h[0] * 5:
            val = '7'
        elif h[:4] == h[0] * 4 or h[1:] == h[1]*4:
            val = '6'
        elif h == h[0]*2 + h[2]*3 or h == h[0]*3 + h[3]*2:
            val = '5'
        elif h[:3] == h[0]*3 or h[1:4] == h[1]*3 or h[2:] == h[2]*3:
            val = '4'
        else:
            pairCount = 0
            for i in range(4):
                if h[i] == h[i+1]:
                    pairCount += 1
            if pairCount == 2:
                val = '3'
            elif pairCount == 1:
                val = '2'
            else:
                val = '1'
        bestHand = max(val, bestHand)
    return bestHand
        

cardMap_p1 = {'2':'a', '3':'b', '4':'c', '5':'d', '6':'e', '7':'f', '8':'g', '9':'h', 'T':'i', 'J':'j', 'Q':'k', 'K':'l', 'A':'m'}
cardMap_p2 = {'2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', 'T':'j', 'J':'a', 'Q':'k', 'K':'l', 'A':'m'}
def replaceCards(hand):
    for c in cardMap_p2:
        hand = hand.replace(c, cardMap_p2[c])
    return hand


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    lines = sorted(lines, 
        key=lambda x: handType(x.split()[0]) + replaceCards(x.split()[0])
    )
    total = 0 
    for i in range(len(lines)):
        bid = int(lines[i].split()[1])
        total += bid*(i+1)
    print(total)