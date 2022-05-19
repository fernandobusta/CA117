#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(1, V + 1):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


class BFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.bfs(s)

    def bfs(self, s):
        queue = [s]
        self.marked[s] = True

        while queue:
            v = queue.pop(0)
            for w in self.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.parent[w] = v
                    self.marked[w] = True

    # Return True if there is a path from s to v
    def hasPathTo(self, v):
        return self.marked[v]

    # Return path from s to v (or None should one not exist)
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]


def main():
    for line in sys.stdin:
        f, s, g, u, d = line.strip().split()
        f = int(f)
        s = int(s)
        g = int(g)
        u = int(u)
        d = int(d)

    g = Graph(f)
    for floor in range(1, f):
        u_connect = floor + u
        d_connect = floor - d
        if 0 < u_connect <= f:
            g.addEdge(floor, u_connect)
        if 0 < d_connect <= f:
            g.addEdge(floor, d_connect)

    paths = BFSPaths(g, s)

    #print(paths.hasPathTo(g))
    print(paths.PathTo(g))

if __name__ == '__main__':
    main()
