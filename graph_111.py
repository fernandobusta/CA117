#!/usr/bin/env python3

class Graph(object):

    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        #if we visited v oon our DFS from s
        #then ther is a path from s to v
        return self.visited[v]

    def pathTo(self, v):
        #return the path from s to v should there be one
        if not self.hasPathTo(v):
            return None
        path = [v]
        #while we are not at our destination
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        #abouve builds the path working backwards from v to s
        #we want the path from s to v so reverse the latter
        return path[::-1]
