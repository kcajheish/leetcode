from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False

        return self._hasPathSum(root, target_sum, 0)

    def _hasPathSum(self, node, target_sum, current_sum):
        # no more nodes to visit, can never meet the target
        if not node:
            return False

        # calculate current sum so far
        current_sum += node.val

        # if node is leaf, check if current sum meet the target
        if not node.left and not node.right:
            return current_sum == target_sum

        # check if left/right subtree has path that accumulates the target
        is_left_reached = self._hasPathSum(node.left, target_sum, current_sum)
        is_right_reached = self._hasPathSum(node.right, target_sum, current_sum)
        return is_left_reached or is_right_reached