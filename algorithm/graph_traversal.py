from collections import defaultdict

class CheckConnectivity:
    def check_connect_dfs(self, edges, start):
        adj = self.build_adj(edges)
        visited = [False] * len(adj)
        self.dfs(start, adj, visited)
        return all(visited)

    def check_connect_bfs(self, edges, start):
        adj = self.build_adj(edges)
        q = [start]
        visited = [False] * len(adj)
        distance = [0] * len(adj)
        while q:
            n = q.pop(0)
            if visited[n]:
                continue
            visited[n] = True
            for u in adj[n]:
                q.append(u)
                distance[u] = distance[n] + 1
        return all(visited)

    def dfs(self, n, adj, visited):
        if visited[n]:
            return

        visited[n] = True
        for u in adj[n]:
            self.dfs(u, adj, visited)

    def build_adj(self, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

edges_a = [
    (0, 1),
    (1, 4),
    (1, 2),
    (2, 3),
    (2, 5),
    (5, 6)
]

edges_b = [
    (0, 1),
    (1, 4),
    (2, 3),
    (2, 5),
    (5, 6)
]

cc = CheckConnectivity()
assert cc.check_connect_bfs(edges_a, 0) == True
assert cc.check_connect_bfs(edges_b, 0) == False
assert cc.check_connect_dfs(edges_a, 0) == True
assert cc.check_connect_dfs(edges_b, 0) == False


class CheckCycle:
    def has_cycle_dfs(self, edges, start):
        adj = self.build_adj(edges)
        seen = [False] * len(adj)
        cycle = []
        for u in adj:
            if seen[u]:
                continue
            self.dfs(adj, seen, cycle, -1, u)
        return bool(cycle)

    def dfs(self, adj, seen, cycle, u, v):

        seen[v] = True
        for w in adj[v]:
            if cycle:
                return

            if not seen[w]:
                self.dfs(adj, seen, cycle, v, w)
            elif w != u:
                cycle.append(v)
                cycle.append(w)

    def build_adj(self, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

cc = CheckCycle()
edges_with_cycle = [
    (0, 1),
    (1, 2),
    (1, 3),
    (2, 3)
]
ediges_wo_cycle = [
    (0, 1),
    (1, 2),
    (1, 3)
]
assert cc.has_cycle_dfs(edges_with_cycle, 0) == True
assert cc.has_cycle_dfs(ediges_wo_cycle, 0) == False

class CheckBipartiteness:
    def check(self, edges):
        adj = self.build_adj(edges)
        state = [None] * len(adj)
        seen = [False] * len(adj)
        pair = []
        for n in adj:
            self.dfs(adj, n, seen, state, pair)
        return bool(pair)

    def dfs(self, adj, v, seen, state, pair):
        seen[v] = True
        for w in adj[v]:
            if pair:
                return
            if not seen[w]:
                if state[v] == 'R':
                    state[w] == 'B'
                else:
                    state[w] = 'R'
                self.dfs(adj, w, seen, state, pair)
            elif state[v] == state[w]:
                pair.append(v)
                pair.append(w)

    def build_adj(self, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj
cb = CheckBipartiteness()
edges_with_cycle = [
    (0, 1),
    (1, 2),
    (1, 3),
    (2, 3)
]
ediges_wo_cycle = [
    (0, 1),
    (1, 2),
    (1, 3)
]
assert cb.check(edges_with_cycle) == True
assert cb.check(ediges_wo_cycle) == False