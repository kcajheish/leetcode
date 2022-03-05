from collections import defaultdict

class TopologicalSort:
    """
    given directed acyclic graph(DAG), find the path

    acyclic: graph does not has cycle, which imply path will not visit same node twice.
    """
    def sort(self, edges, n):
        graph = self.build_graph(edges)
        seen = [0] * (n+1)
        order = []
        # for node in graph:
        for node in range(1, n+1):
            if seen[node] == 2:
                continue
            if self.dfs(graph, node, seen, order) == False:
                return []
        self.reverse(order)
        return order

    def dfs(self, graph, node, seen, order):
        seen[node] = 1
        for neighbor in graph[node]:
            if seen[neighbor] == 2:
                continue
            elif seen[neighbor] == 1:
                return False
            has_cycle = self.dfs(graph, neighbor, seen, order) == False
            if has_cycle:
                return False
        order.append(node)
        seen[node] = 2

    def build_graph(self, edges):
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
        return graph

    def reverse(self, arr):
        left, right = 0, len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

edges = [
    (1,2),
    (2,3),
    (3,6),
    (4,1),
    (4,5),
    (5,2),
    (5,3)
]
edges_with_cycle = [
    (1,2),
    (2,1),
    (2,3),
    (3,6),
    (4,1),
    (4,5),
    (5,2),
    (5,3)
]
n = 6

ts = TopologicalSort()
order_1 = ts.sort(edges, n)
ts = TopologicalSort()
order_2 = ts.sort(edges_with_cycle, n)
assert order_1 ==  [4,5,1,2,3,6]
assert order_2 ==  []
