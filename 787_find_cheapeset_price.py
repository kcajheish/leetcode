"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        costs = defaultdict(lambda: float('inf'))
        for start, stop, cost in flights:
            graph[start].append(
                (stop, cost)
            )

        costs[src] = 0

        queue = [(src, 0, 0)]

        while queue:
            start, visits, total= queue.pop(0)
            if visits > k or start == dst:
                continue
            for stop, cost in graph[start]:
                if cost + total < costs[stop]:
                    costs[stop] = cost + total
                    queue.append(
                        (stop, visits + 1, cost + total)
                    )
                    print('stop', stop,'visits', visits+1, 'cost', costs[stop])
                else:
                    continue

        return costs[dst] if costs[dst] < float('inf') else -1
s = Solution()
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
r = s.findCheapestPrice(n, flights, src, dst, k)
print(r)

n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
r = s.findCheapestPrice(n, flights, src, dst, k)
print(r)