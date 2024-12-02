# python 1.py input.txt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()
with open(args.input_file, 'r') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

'''
max flow min cut

find edges traversed from point a to point b
without using any of the previously found edges, traverse new path to b
if no new paths possible, then the set of shared edges by all paths are the minimum cut

example line:
rzs: qnr cmg lsr rsh

'''

class Node:
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return f"Node({self.identifier})"


class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        self.nodes = [Node(i) for i in range(size)]

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

        def bfs(self, parent, source, sink):
        visited = [False] * self.size
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[sink]


    def edmonds_karp(self, source, sink):
        parent = [-1] * self.size
        max_flow = 0

        while self.bfs(parent, source, sink):
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


if __name__ == "__main__":
    nodes = []
    for line in lines:
        input = line.split(':')
        name = input[0]
        peers = input[1].split(' ')

