from typing import List
from collections import defaultdict

class Solution:
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [False] * numCourses
        onStack = [False] * numCourses
        taken = []
        self.hasCycle = False
        graph = self.build_graph(prerequisites)

        for course in range(numCourses):
            if not visited[course]:
                self.dfs(course, graph, taken, visited, onStack)
        return taken if not self.hasCycle else []

    def build_graph(self,pairs):
        graph = defaultdict(list)
        for node, to_node in pairs:
            graph[node].append(to_node)
        return graph

    def dfs(self, course, graph, taken, visited, onStack):
        visited[course] = True
        onStack[course] = True
        for neighbor in graph[course]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, taken, visited, onStack)
            elif onStack[neighbor]:
                self.hasCycle = True
        taken.append(course)
        onStack[course] = False


