from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.build_graph(edges)
        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        while n < 2:
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                n -= 1
                neighbor = graph[leaf].pop
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


    def build_graph(self, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph