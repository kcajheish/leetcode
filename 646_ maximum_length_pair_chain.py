def findLongestChain_greedy(pairs):
    """
    time complexity: O(NlnN)
    space complexity: O(N)
    """
    pairs.sort(key=lambda pair: pair[1])
    results = [[-float('inf'), -float('inf')]]
    for pair in pairs:
        left, right = pair
        if right > results[-1][1]:
            results.append(pair)
    return len(results) - 1


def findLongestChain_dp(pairs):
    """
    time complexity: O(N^2)
    space complexity: O(N)
    """
    dp = [1] * len(pairs)
    for i in range(len(pairs)):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )
    return max(dp)


pairs = [[1,2],[2,3],[3,4]]

# findLongestChain(pairs)