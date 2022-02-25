from typing import List
import heapq
class Solution:
    def minCostConnectPointsKruskal(self, points: List[List[int]]) -> int:
        """
        time complexity
        space complexity
        """
        union = [i for i in range(len(points))]
        heap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i], points[j]
                heapq.heappush(heap, (self.man_distance(a, b),i, j))

        connect = 1
        dist = 0
        while connect < len(points):
            d, x, y = heapq.heappop(heap)
            x_root = self.find(union, x)
            y_root = self.find(union, y)
            if x_root != y_root:
                union[x_root] = y_root
                dist += d
                connect += 1
        return dist

    def minCostConnectPointsPrime(self, points: List[List[int]]) -> int:
        """
        time complexity: O(N^2)
        note: N^2lnN without pruning

        idea:
        select first point, as base of the tree.
        find distance from first point to any other point; ignore point if it is already in the tree
        point that has least distance will be next pick for tree; ignore point if it is already in the tree
        """
        heap = []
        current = 0
        visits = {current}
        distances = 0
        while len(visits) < len(points):
            for i in range(len(points)):
                if i in visits:
                    continue
                a, b = points[current], points[i]
                dst =  self.man_distance(a, b)
                heapq.heappush(heap, (dst, i))
            while heap[0] in visits:
                heapq.heappop(heap)
            shortest, current = heapq.heappop(heap)
            distances += shortest
            visits.add(current)
        return distances

    def minCostConnectPointsPrimeCompleteGraph(self, points: List[List[int]]) -> int:
        current = 0
        visits = {current}
        dst = [float('inf')] * len(points)
        distances = 0
        while len(visits) < len(points):
            for i in range(len(points)):
                if i in visits:
                    continue
                dst[i] = min(dst[i], self.man_distance(points[i], points[current]))
            shortest, current = min(
                (
                    (d, k) for k, d in enumerate(dst)
                    if k not in visits
                )
            )
            distances += shortest
            visits.add(current)
        return distances


    def man_distance(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def find(self, union, i):
        if i == union[i]:
            return i
        return self.find(union, union[i])