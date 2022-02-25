from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(prerequisites)
        for course in range(numCourses):
            taken = [False] * numCourses
            path = [False] * numCourses
            if not self.dfs(graph, course, taken, path):
                return False
        return True

    def dfs(self, graph, course, taken, path):
        taken[course] = True
        path[course] = True
        res = True
        for neighbor in graph[course]:
            if path[neighbor]:
                return False
            if taken[neighbor]:
                continue
            res = res and self.dfs(graph, neighbor, taken, path)
        path[course] = False
        return res

    def build_graph(self, prerequisites):
        graph = defaultdict(list)
        for course, required in prerequisites:
            graph[course].append(required)
        return graph
