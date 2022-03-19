from collections import defaultdict

class Kosaraju:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_sc(self):
        visited = [False] * self.V
        self.dfs(0, visited)
        if any([visit == False for visit in visited]):
            return False

        reverse_g = self.reverse_graph()
        visited_in_reverse = [False] * self.V
        reverse_g.dfs(0, visited_in_reverse)
        if any([visit == False for visit in visited]):
            return False
        return True

    def dfs(self, node, visited):
        visited[node] = True
        for neighbor in self.graph:
            if visited[neighbor]:
                continue
            self.dfs(neighbor, visited)

    def reverse_graph(self):
        reverse = Kosaraju(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                reverse.add_edge(neighbor, node)
        return reverse

# Create a graph given in the above diagram
g1 = Kosaraju(5)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 0)
g1.add_edge(2, 4)
g1.add_edge(4, 2)
assert g1.is_sc() == True

g2 = Kosaraju(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
assert g2.is_sc() == False