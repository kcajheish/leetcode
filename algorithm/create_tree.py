"""
create tree from heap
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_tree(nums):
    def traverse(nums, i):
        if i >= len(nums):
            return

        node = Node(nums[i])
        node.left = traverse(nums, 2 * i + 1)
        node.right = traverse(nums,  2 * i + 2)
        return node
    return traverse(nums, 0)
