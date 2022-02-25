"""
inorder traversal: visit in order of left, parent, right.
recursion: after done visiting left subtree, get current node value, and continue exploring right subtree
iterative: keep visiting left subtree until no node can be reached, store value and visiting right
"""

def inorderTraversal_recursive(root):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    def traverse(node, results):
        if node is None:
            return
        results.append(node.val)
        traverse(node.left)
        traverse(node.right)
    results = []
    traverse(root, results)
    return results

def inorderTraversal_iterative(root):
    stack = []
    results = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        results.append(root.val)
        root = root.right
    return results