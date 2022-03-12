"""
spanning tree:
it's a subset of the graph; all nodes of graph and part of the edges
weight = sum of the edge weight
two extreme: maximum and minimun spanning tree
"""
import heapq


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if self.size[root_u] == self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_u] += 1
        elif self.size[root_u] > self.size[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v


class Kruskal:
    """
    idea:
    given edges, pick out smallest edge one by one. if the edge already belongs to connected component, ignore it.
    until all nodes are connected, we have minimun spanning tree
    """
    def mst(self, edges, n):
        edges.sort(key=lambda edge: edge[2])
        connects = n - 1
        uf = UF(n)
        cost = 0
        while connects:
            u, v, w = edges.pop(0)

            root_u = uf.find(u)
            root_v = uf.find(v)
            if root_u != root_v:
                uf.union(u, v)
                connects -= 1
                cost += w
        return cost


class Prime:
    def mst(self, edges, n):
        """
        time complexity: O(n+mlogm)
        """
        adj = [[] for i in range(n)]
        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))

        q = [(0, 0)]
        seen = [False] * n
        cost = 0
        while q:
            weight, u = heapq.heappop(q)
            # print(f"node {u}, weight {weight} cost {cost + weight}")
            if seen[u]:
                continue
            seen[u] = True
            cost += weight
            for w, v in adj[u]:
                if seen[v]:
                    continue
                heapq.heappush(q, (w, v))
        return cost

edges = [
    (0, 1, 10), # u, v, w
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4
ksk = Kruskal()
assert ksk.mst(edges, n) == 19

edges = [
    (0, 1, 10), # u, v, w
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4
prime = Prime()
assert prime.mst(edges, n) == 19
