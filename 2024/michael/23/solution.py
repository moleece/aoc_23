import sys

def build_graph(lines):
    g = {}
    vs = set()
    for line in lines:
        a, b = line.split('-')
        vs.add(a)
        vs.add(b)
        if a not in g:
            g[a] = set()
        g[a].add(b)
        if b not in g:
            g[b] = set()
        g[b].add(a)
    return vs, g

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]

    vs, g = build_graph(lines)
    # # Find triangles
    # ts = set()
    # for line in lines:
    #     a, b = line.split('-')
    #     for c in g[a]:
    #         if c in g[b]:
    #             ts.add(tuple(sorted([a,b,c])))

    # # Count ones with a 't' in them
    # count = 0
    # for t in ts:
    #     for v in t:
    #         if v[0] == 't':
    #             count += 1
    #             break

    # print(count)

    ## P2
    # Find triangles
    ts = set()
    for line in lines:
        a, b = line.split('-')
        for c in g[a]:
            if c in g[b]:
                ts.add(tuple(sorted([a,b,c])))
    ts = list(ts)

    while len(ts) > 0:
        # Find fully connected components one size larger
        nextTs = set()
        for t in ts:
            for n in g[t[0]]:
                linked = True
                for m in t[1:]:
                    if n not in g[m]:
                        linked = False
                        break
                if linked:
                    nextTs.add(tuple(sorted(list(t) + [n])))
        if len(nextTs) == 0:
            break
        ts = list(nextTs)
    
    print(','.join(ts[0]))

    
