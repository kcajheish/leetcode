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

"""
successor graph:
every edges can be expressed by a function; the param is node, the return is successor node.
every node has out degree of one(one edge outward).
"""
def succ(node):
    """
    to find node after k steps, it takes O(n) time
    how to improve time complexity??
    """
    return node + 1

def step(start, step):
    end = start
    while step:
        end = succ(end)
        step -= 1
    return end

def precalculate(n, k):
    """
    precalculate destination after k steps
    """
    dp = [[None] * n for i in range(k)]

    for power in range(k):
        for node in range(n):
            dp[power][node] = step(node, pow(2, power))
    # print(dp)
    return dp

def query(start, step, dp):
    node = start
    count = 0
    while step:
        if step % 2:
            # print(f"old node = {node} new node ={dp[count][node]} step = {pow(2, count)}")
            node = dp[count][node]

        step = step//2
        count += 1

    return node

assert step(0, 5) == 5
assert precalculate(3, 3) == [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
assert query(0, 11, precalculate(10, 10)) == 11

class Floyd:
    def start_of_cycle(self, start):
        """
        approach 1: keep track of node along the path. if a node is visited twice, we find the start of cycle;
        time complexity: O(n)
        space complexity: O(n)

        to save space, use fast and slow pointer.
        """
        slow, fast = self.succ(start), self.succ(self.succ(start))
        while slow != fast:
            slow = self.succ(slow)
            fast = self.succ(self.succ(fast))

        fast = start
        while slow != fast:
            slow = self.succ(slow)
            fast = self.succ(fast)
        return fast

    def succ(self, n):
        path = {
            0: 1,
            1: 3,
            3: 5,
            5: 7,
            7: 9,
            9: 5
        }
        return path[n]

fld = Floyd()
assert fld.start_of_cycle(0) == 5