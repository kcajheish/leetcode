import unittest

"""
https://leetcode.com/problems/coin-change/discuss/1320117/Python-2-approaches-%3A-BFS-Top-down-Memoized-recursion-%3A-Explained-%2B-visualized
https://www.geeksforgeeks.org/coin-change-dp-7/
"""

def coinChange_bf(coins ,n):
    """
    breath first search
    idea: start by pick one coin and another. which ever meet the target first is our anser
    time complexity: O(M**n) given M is minimum coins and n is number of demonimator
    """
    q = list()
    q.append(n)
    level = 0
    while q:
        for i in range(len(q)):
            target = q.pop(0)
            for coin in coins:
                diff = target - coin
                print(target, coin, diff)
                if diff == 0:
                    return level + 1
                elif diff < 0:
                    continue
                else:
                    q.append(diff)
        level += 1
    return -1


def coinChangeDP(coins, n):
    """
    space complexity: O(n)
    time complexity: O(coins * n)

    idea: find minimal coins that add up to n.
    whether coin selection can meet target n depends on previous selection
    -> dp
    """
    dp = [float('inf')] * (n+1)

    # no coin is needed to make up zero
    dp[0] = 0

    # look for number of coins needed for target in (0, 1, ...n)
    for target in range(1, n+1):
        for coin in coins:
            if target - coin >= 0:
                dp[target] = min(dp[target],dp[target-coin] + 1)
    if dp[n] == float('inf'):
        return -1
    return dp[n]






