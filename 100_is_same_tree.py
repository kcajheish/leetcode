def isSameTree_recursive(p, q):
    """
    check whether two tree are the same
    start form the root of both tree.
    examine each node on both tree.
    if node value is the same and left subree and right subtree are also the same.
    then the tree is the same.ß
    """
    if not p and not q:
        return True
    elif not p or not q:
        return False

    return p.val == q.val and isSameTree_recursive(p.left, q.left) and isSameTree_recursive(p.right, q.right)


def isSameTree_recursive(p, q):
    """
    iterative version
    stack can be replaced by queue, which is useful for BFS
    """
    stack = [(p, q)]
    while stack:
        p, q  = stack.pop()
        if not p and not q:
            continue
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        stack.append((p.left, q.left))
        stack.append((p.right, q.right))
    return True