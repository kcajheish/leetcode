from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root.left, root.right)

    def mirror(self, left, right):
        """
        recursive
        if a tree is mirror-image, its left child and right child have same value.
        its grand children with same distance to the mirror line also have same value
        """
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val \
            and self.mirror(left.left, right.right) \
            and self.mirror(left.right, right.left)

    def isSymmetricIterative(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop(0)
            if not left and not right:
                continue
            elif not left or not right or left.val != right.val:
                return False
            else:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        return True

