"""
Clone Graph
in python,
append and pop operation take O(N) in List, constant O(1) in dequeue
"""

from collections import dequeue

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        """
        Breath Frist Search
        """
        q = dequeue([node])
        visited = {node: Node(node.val, [])}
        while q:
            visited_node = q.pop()
            for neighbor in visited_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                visited[visited_node].neighbors.append(visited[neighbor])

        return visited[node]

    def cloneGraph2(self, node):
        """
        Depth First Search
        """
        if not node:
            return

        stack = [node]
        visited = {node: Node(node.val, [])}
        while stack:
            visited_node = stack.pop()
            for neighbor in visited_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                visited[visited_node].neighbors.push(visited[neighbor])
        return visited[node]


    def cloneGraph3(self, node):
        """
        DFS Recursive version
        """
        if not node:
            return None
        visited = {node: Node(node.val, [])}
        clone_graph = self.dfs(visited, node)
        return clone_graph


    def dfs(self, visited, node):
        if node in visited:
            return visited[node]

        visited[node] = Node(node.val, [])
        for neighbor in node.neighbors:
            visited[node].neighbors.push(self.dfs(visited, neighbor))

        return visited[node]





