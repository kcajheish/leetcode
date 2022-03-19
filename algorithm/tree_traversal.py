from collections import defaultdict

class TreeTraversal:
    def __init__(self):
        self.graph = defaultdict(list)

    def dfs(self, curr, prev):
        for neighbor in self.graph[curr]:
            if neighbor != prev:
                self.dfs(neighbor, curr)
        # print(curr)

    def count_nodes(self, curr, prev):
        count = 1
        for neighbor in self.graph[curr]:
            if neighbor != prev:
                count += self.count_nodes(neighbor, curr)
        return count

    def max_length(self, curr, prev):
        """
        max length from root to leaf
        """
        max_so_far = 0
        for neighbor in self.graph[curr]:
            if neighbor != prev:
                max_so_far = max(max_so_far, self.max_length(neighbor, curr))
        return max_so_far + 1

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


tt = TreeTraversal()
tt.add_edge(1,2)
tt.add_edge(1,3)
tt.add_edge(1,4)
tt.add_edge(2,5)
tt.add_edge(2,6)
tt.add_edge(6,8)
tt.add_edge(4,7)

tt.dfs(1, 0)
assert tt.max_length(1, 0) == 4
assert tt.count_nodes(1, 0) == 8

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree:
    def create_tree(self, nums, i):
        if i >= len(nums):
            return
        elif not nums[i]:
            return None
        node = Node(nums[i])
        node.left = self.create_tree(nums, 2*i+1)
        node.right = self.create_tree(nums, 2*i+2)
        return node

    def in_order(self, node, order):
        if not node:
            return
        self.in_order(node.left, order)
        order.append(node.val)
        self.in_order(node.right, order)

    def post_order(self, node, order):
        if not node:
            return
        self.post_order(node.left, order)
        self.post_order(node.right, order)
        order.append(node.val)

    def pre_order(self, node, order):
        if not node:
            return
        order.append(node.val)
        self.pre_order(node.left, order)
        self.pre_order(node.right, order)

heap = [1, 2, 3, 4, 5, None, 7, None, None, 6]
bt = BinaryTree()
root = bt.create_tree(heap, 0)
in_order = []
bt.in_order(root, in_order)
post_order = []
bt.post_order(root, post_order)
pre_order = []
bt.pre_order(root, pre_order)

assert in_order == [4, 2, 6, 5, 1, 3, 7]
assert post_order == [4, 6, 5, 2, 7, 3, 1]
assert pre_order == [1, 2, 4, 5, 6, 3, 7]
