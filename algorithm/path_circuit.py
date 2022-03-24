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


if __name__ == '__main__':
    unittest.main()