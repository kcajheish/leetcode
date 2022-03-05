from collections import defaultdict
import heapq


class BellmanFord:
    """
    given edges, nodes and source node, return shortest path from source to all nodes

    explore from source node, reduce the distance if there is a shorter path to any given node.
    if no distance can be reduced, we have shortest path
    """
    def shortest_path(self, edges, n, source):
        """
        n: number of nodes
        edge: (a, b, w), meaning edge from node a to node b has weight of w

        time complexity: O(mn) where n is number of node, and m is number of edges.

        problems: final distance can be found faster than n-1 iterations.
        how can we terminate earlier?

        why shortest path is guaranteed after n iteration?
        https://riptutorial.com/algorithm/example/24029/why-do-we-need-to-relax-all-the-edges-at-most--v-1--times
        https://stackoverflow.com/questions/49263065/why-need-node-number-1-iterations-in-bellman-ford-algorithm-to-find-shortest
        """
        distances = [float('inf')] * n
        distances[source] = 0
        for _ in range(n-1):
            for start, end, weight in edges:
                distances[end] = min(distances[end], distances[start]+weight)
        return distances

    def shortest_path_faster(self, edges, n, source):
        """
        explore the path only when distance can be reduce.
        if distance cannot be reduced, we have the shortest path
        """
        distances = [float('inf')] * n
        distances[source] = 0
        graph = self.build_graph(edges)
        queue = [source]
        while queue:
            start = queue.pop(0)
            for end, weight in graph[start]:
                if distances[end] > distances[start] + weight:
                    distances[end] = distances[start] + weight
                    queue.append(end)

        return distances

    def build_graph(self, edges):
        graph = defaultdict(list)
        for start, end, weight in edges:
            graph[start].append((end, weight))
        return graph

n = 3
src = 0
edges = [
    (0, 1, 1),
    (1, 2, 3),
    (0, 2, 1)
]
bf = BellmanFord()
distances = bf.shortest_path(edges, n, src)
assert distances == [0, 1, 1]

distances_faster = bf.shortest_path_faster(edges, n, src)
assert distances_faster == [0, 1, 1]

class Dijkstra:
    """
    given edges, nodes, source, return shortest path from source to all nodes

    when explore the graph, always look for the nearest node first.
    after all edges and nodes are visited once, we have shortest path.

    time complexity: mlogm + n

    Dijkstra is more efficient than Bellman Ford, since we always look nearest node
    rather than randomly visit all node.
    """
    def shortest_path(self, edges, n, source):
        distances = [float('inf')] * n
        distances[source] = 0
        seen = [False] * n
        graph = self.build_graph(edges)
        queue = [(0, source)]
        while queue:
            start, dst_so_far = heapq.heappop(queue)
            if seen[start]:
                continue
            seen[start] = True
            for neighbor, weight in graph[start]:
                if distances[neighbor] > distances[start] + weight:
                    distances[neighbor] = distances[start] + weight
                    heapq.heappush(queue, (distances[neighbor], neighbor))
        return distances


    def build_graph(self, edges):
        graph = defaultdict(list)
        for start, end, weight in edges:
            graph[start].append((end, weight))
        return graph

n = 3
src = 0
edges = [
    (0, 1, 1),
    (1, 2, 3),
    (0, 2, 1)
]
ds = Dijkstra()
distances = ds.shortest_path(edges, n, src)
assert distances == [0, 1, 1]


class FloydWarshall:
    """
    given start and end point, pick an intermediate point that can shorten the path between them

    time complexity: O(n^3)

    easy to implement, but note that use it when graph is small enough that this algo runs fast enough
    """
    def shortest_path(self, adj, n, source):
        distance = self.build_distance_matrix(adj, n)
        for mid in range(n):
            for start in range(n):
                for end in range(n):
                    distance[start][end] = min(
                        distance[start][end], distance[start][mid] + distance[mid][end]
                    )
        return distance[source]

    def build_distance_matrix(self, adj, n):
        matrix = [
            [float('inf')] * n
                for _ in range(n)
        ]
        for row in range(n):
            for col in range(n):
                if row == col:
                    matrix[row][col] = 0
                elif adj[row][col] != 0:
                    matrix[row][col] = adj[row][col]
        return matrix
"""
    1       7
(0) - > (1) -> (2)
 \       |      /
 5\     1|     /5
   \     v    /
    >   (3)  <
"""
# adjacency matrix: store edges in 2d matrix, which is useful for read,
# but it consumes lots of memory if graph is big.
adj = [
    [0, 1, 0, 5],
    [0, 0, 7, 1],
    [0, 0, 0, 5],
    [0, 0, 0, 0]
]
n = 4
source = 0
fw = FloydWarshall()
shortest = fw.shortest_path(adj, n, source)
assert shortest == [0, 1, 8, 2]
