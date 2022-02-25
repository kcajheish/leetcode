def findFrequentTreeSum_recursive(root):
    if not root:
        return []

    def treeSum(node, count):
        if not node:
            return 0
        left_sum = treeSum(node.left, count)
        right_sum = treeSum(node.right, count)
        total = left_sum + right_sum + node.val
        count[total] = count.get(total, 0) + 1
        return total

    count = dict()
    treeSum(root, count)
    most_often = max(count.values())
    return [f for f in count if count[f] == most_often]
