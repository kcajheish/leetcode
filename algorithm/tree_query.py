import unittest
from collections import defaultdict

class SubtreeQuery:
    def __init__(self):
        self.graph = defaultdict(list)
        self.sizes = []
        self.values = []
        self.index = 0

    def make_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def explore(self, node):
        visited = [False] * len(self.graph)
        self.values = [None] * len(self.graph)
        self.sizes = [None] * len(self.graph)
        self.dfs(node, visited)

    def dfs(self, node, visited):
        visited[node] = True
        size = 1
        current_index = self.index
        self.index += 1
        for next_node in self.graph[node]:
            if not visited[next_node]:
                size += self.dfs(next_node, visited)
        self.values[current_index] = node
        self.sizes[current_index] = size
        return size

    def query(self, node):
        start = 0
        while self.values[start] != node:
            start += 1
        sum_so_far = 0
        for i in range(start, start+self.sizes[start]):
            sum_so_far += self.values[i]
        return sum_so_far


class TestTreeQuery(unittest.TestCase):
    def setUp(self):
        self.sq = SubtreeQuery()
        self.sq.make_edge(0, 1)
        self.sq.make_edge(1, 5)
        self.sq.make_edge(0, 2)
        self.sq.make_edge(0, 3)
        self.sq.make_edge(0, 4)
        self.sq.make_edge(3, 6)
        self.sq.make_edge(3, 7)
        self.sq.make_edge(3, 8)
        self.sq.explore(0)

    def test_query_root(self):
        self.assertEqual(self.sq.query(0), 36)

    def test_query_subtree(self):
        self.assertEqual(self.sq.query(3), 24)

    def test_query_null_link(self):
        self.assertEqual(self.sq.query(8), 8)

if __name__ == '__main__':
    unittest.main()
