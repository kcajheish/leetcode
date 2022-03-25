from collections import defaultdict
import unittest
class EulerianPath:
    def __init__(self):
        self.graph = defaultdict(list)
        self.E = 0
        self.V = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.E += 1
        self.V = len(self.graph)

    def degree(self, u):
        return len(self.graph[u])

    def non_isolated_node(self):
        for v in self.graph:
            if self.degree(v) > 0:
                return v

    def dfs(self, visited_edges, path, from_node):
        path.append(from_node)
        for to_node in self.graph[from_node]:
            if not visited_edges[from_node][to_node]:
                visited_edges[from_node][to_node] = True
                visited_edges[to_node][from_node] = True
                self.dfs(visited_edges, path, to_node)

    def eulerian(self):
        # check graph has edges
        if self.E == 0:
            return

        # cycle has even degree on every node
        odd_degree = 0
        for v in self.graph:
            if self.degree(v) % 2 != 0:
                odd_degree += 1

        if odd_degree > 2 or odd_degree == 1:
            raise Exception('not Eulerian graph')

        s = self.non_isolated_node()

        path = []
        visited_edges = [[False] * self.V for _ in range(self.V)]
        self.dfs(visited_edges, path, s)
        if odd_degree == 0:
            return 'cycle', path
        else:
            return 'path', path


class TestEulerianCycle(unittest.TestCase):

    def test_cycle(self):
        ec = EulerianPath()
        ec.add_edge(0, 1)
        ec.add_edge(1, 2)
        ec.add_edge(2, 0)
        cycle = ec.eulerian()
        expect = 'cycle', [0,1,2,0]
        self.assertEqual(cycle, expect)

    def test_path(self):
        ec = EulerianPath()
        ec.add_edge(0, 1)
        ec.add_edge(1, 2)
        ec.add_edge(2, 3)
        expect = 'path', [0, 1, 2, 3]
        self.assertEqual(ec.eulerian(), expect)

    def test_three_odd(self):
        ec = EulerianPath()
        ec.add_edge(0, 1)
        ec.add_edge(1, 2)
        ec.add_edge(2, 3)
        ec.add_edge(3, 1)
        ec.add_edge(2, 3)
        ec.add_edge(2, 4)
        self.assertRaises(Exception, ec.eulerian)

class Hamiltonian:
    def check_path(self, V, edges):
        graph = self.build_graph(edges)
        seen = [False for i in range(V)]
        for i in range(V):
            path = []
            if self.dfs(graph, i, seen, 0, V, path):
                # print('hamiltonian path:', path)
                return True
        return False

    def dfs(self, graph, node, seen, num, V, path):
        path += [node]
        seen[node] = True
        num += 1
        if num == V:
            return True

        for next_node in graph[node]:
            if not seen[next_node]:
                if self.dfs(graph, next_node, seen, num, V, path):
                    return True
        seen[node] = False
        path.pop()
        return False

    def build_graph(self, edges):
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g

h = Hamiltonian()
N = 4
edges =  [ (0,1), (1,2), (2,3), (1,3)]
assert h.check_path(N, edges) == True

N = 4
edges = [(0,1), (1,2), (1,3)]
assert h.check_path(N, edges) == False
if __name__ == '__main__':
    unittest.main()