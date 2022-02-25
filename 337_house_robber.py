def rob_dp(root):
    """
    dp with memoization
    time complexity: O(N), proportinal to number of node being visited
    space complexity: O(N)
    """
    def _rob(root, memo):
        if not root:
            return 0
        if root in memo:
            return memo[root]

        rob_this = root.val
        if root.left:
            rob_this += _rob(root.left.left, memo) + _rob(root.left.right, memo)
        if root.right:
            rob_this += _rob(root.right.left, memo) + _rob(root.right.right, memo)
        not_rob = _rob(root.left, memo) + _rob(root.right, memo)
        res = max(rob_this, not_rob)
        memo[root] = res
        return res
    return _rob(root, {})

def rob_dp_v2(root):
    """
    split the state into rob and not rob for every node; optimize space complexity
    time complexity: O(N), proportinal to number of node being visited
    space complexity: O(1)
    """
    def _rob(root):
        if not root:
            return 0, 0

        left = _rob(root.left)
        right = _rob(root.right)

        rob_this = left[1] + right[1] + root.val
        not_rob = max(left) + max(right)

        return rob_this, not_rob
    return max(_rob(root))