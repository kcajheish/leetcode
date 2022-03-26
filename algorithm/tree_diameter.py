from collections import defaultdict
import unittest
class TreeDiameter:
    def to_leaf(self, node, visited, graph):
        length = 0
        visited[node] = True
        for to_node in graph[node]:
            if visited[to_node] == False:
                length = max(length, self.to_leaf(to_node, visited, graph)+1)
        visited[node] = False
        return length

    def build_graph(self, edges):
        g = defaultdict(list)
        for this_node, other_node in edges:
            g[this_node].append(other_node)
            g[other_node].append(this_node)
        return g

    def max_length(self, node, edges):
        graph = self.build_graph(edges)
        most = 0
        second = 0

        # if node has one child, it does not have diameter
        if len(graph[node]) == 1:
            return 0

        for next_node in graph[node]:
            visited = [False] * len(graph)
            visited[node] = True # set start node as being visited to avoid backtrack
            length = self.to_leaf(next_node, visited, graph)
            if length > most:
                second = most
                most = length
            elif length > second:
                second = length
        return most + second + 2

class TestDiameter(unittest.TestCase):
    def setUp(self):
        self.diameter = TreeDiameter()

    def test_a_chain(self):
        edges = [
            (0, 1),
            (1, 2),
            (2, 3)
        ]
        self.assertEqual(self.diameter.max_length(0, edges), 0)

    def test_spider_web(self):
        edges = [
            (0, 1),
            (1, 3),
            (1, 4),
            (4, 5),
            (4, 6),
            (0, 2),
            (0, 7),
            (7, 8)
        ]
        self.assertEqual(self.diameter.max_length(0, edges),5)

if __name__ == '__main__':
    unittest.main()
