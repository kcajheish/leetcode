from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBSTDFS(self, root: Optional[TreeNode]) -> bool:
        is_bst, least, largest =  self.is_valid(root)
        return is_bst

    def  is_valid(self, node):
        if not node:
            return True, float('inf'), float('-inf')

        is_left_bst, left_least, left_largest = self.is_valid(node.left)
        is_right_bst, right_least, right_largest = self.is_valid(node.right)

        if not is_left_bst and not is_right_bst:
            return False, None, None

        is_bst = node.val < right_least and node.val > left_largest and is_left_bst and is_right_bst
        least = min(left_least, node.val)
        largest = max(right_largest, node.val)
        return is_bst, least, largest

    def isValidBSTBFS(self, root: Optional[TreeNode]) -> bool:
        # how to do it by bfs
        pass

