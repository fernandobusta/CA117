#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class Islands(object):

    def __init__(self, g):
        self.g = g
        self.marked = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.islands = 0
        self.ccs()

    def ccs(self):
        for s in range(self.g.V):
            # Repeatedly call bfs until every vertex visited.
            # For each call we have a new island.
            if self.marked[s]:
                continue
            self.islands += 1
            self.bfs(s)

    def bfs(self, s):
        queue = [s]
        self.marked[s] = True

        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.parent[w] = v
                    self.marked[w] = True

    def get_islands(self):
        return self.islands

def main():

    V = int(sys.stdin.readline())

    g = Graph(V)

    for line in sys.stdin:

        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

    islands = Islands(g)
    print(islands.get_islands())


if __name__ == '__main__':
    main()
