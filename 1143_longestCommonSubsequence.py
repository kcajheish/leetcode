"""
https://leetcode.com/problems/longest-common-subsequence/discuss/590781/From-Brute-Force-To-DP

"""

def longestCommonSubsequenceBottomUpDP(text1, text2):
    """
    time complexity: M*N
    """
    W2, W1 = len(text2), len(text1)

     # don't use [[0]*m]*n, cuz *n will copy reference
    dp = [[0]*(W2+1) for i in range(W1+1)]

    for i in range(1,W1+1):
        for j in range(1, W2+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    return dp[W1][W2]

def longestCommonSubsequenceRecursive(text1, text2):
    def find_rest(text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return find_rest(text1, text2, i+1, j+1) + 1
        else:
            a = find_rest(text1, text2, i, j+1)
            b = find_rest(text1, text2, i+1, j)
            return max(a, b)
    return find_rest(text1, text2, 0, 0)

def longestCommonSubsequenceRecursiveDP(text1, text2):
    def find_rest(text1, text2, i, j, dp):
        if i == len(text1) or j == len(text2):
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = find_rest(text1, text2, i+1, j+1, dp) + 1
        else:
            a = find_rest(text1, text2, i, j+1, dp)
            b = find_rest(text1, text2, i+1, j, dp)
            dp[i][j] = max(a,b)
        return dp[i][j]
    dp = [[None] * len(text2) for i in range(len(text1))]
    return find_rest(text1, text2, 0, 0, dp)

# r = longestCommonSubsequence("bl", "yby")
# print(r)

