from collections import defaultdict
from tkinter.dnd import dnd_start

class Edge:
    def __init__(self, source, sink, capacity, flow):
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.flow = flow

class EdmondKarp:
    def __init__(self):
        self.graph = defaultdict(list)

    def max_flow(self, source, sink, n):
        """
        find the fewest node from source to sink
        """
        largest_flow = 0
        while True:
            queue = [source]
            parent = [None] * (n+1)
            while queue:
                node = queue.pop(0)
                for edge in self.graph[node]:
                    if edge.capacity > edge.flow and not parent[edge.sink] and edge.sink != source:
                        queue.append(edge.sink)
                        parent[edge.sink] = edge

            if not parent[sink]:
                break
            else:
                edge = parent[-1]
                more_flow = float('inf')
                while edge:
                    more_flow = min(more_flow, edge.capacity-edge.flow)
                    edge = parent[edge.source]
                edge = parent[-1]
                while edge:
                    edge.flow += more_flow
                    edge = parent[edge.source]
                largest_flow += more_flow
        return largest_flow

    def add_edge(self, source, sink, weight):
        edge = Edge(source, sink, weight, 0)
        self.graph[source].append(edge)

ek = EdmondKarp()
ek.add_edge(1,2,5)
ek.add_edge(2,3,6)
ek.add_edge(3,6,5)
ek.add_edge(1,4,4)
ek.add_edge(4,2,3)
ek.add_edge(4,5,1)
ek.add_edge(3,5,8)
ek.add_edge(5,6,2)

assert ek.max_flow(1, 6, 6) == 7