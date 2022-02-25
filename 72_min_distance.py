class Solution:
    def minDistance(self, word1, word2):
        """
        bottom up approach
        """
        H = len(word1)
        W = len(word2)
        dp = [[0] * (W+1) for i in  range(H+1)]

        # to transform empty string it takes n deletions
        for i in range(H+1):
            dp[i][0] = i

        # transform from emptry string, it takes n insertion
        for j in range(W+1):
            dp[0][j] = j

        for i in range(1,H+1):
            for j in range(1, W+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j-1], # delete operations
                        dp[i-1][j-1], # replace
                        dp[i-1][j], # insert
                    )
        return dp[H][W]

