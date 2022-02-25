def isSubsequence_brute_force(s, t):
    count = 0
    j = 0
    for i in range(len(s)):
        while j < len(t):
            if s[i] == t[j]:
                j += 1
                count += 1
                break
            j += 1
    return count == len(s)

def isSubsequence_brute_force_v2(s, t):
    j = 0
    for i in range(len(t)):
        if s[j] == t[i]:
            j += 1

    return j == len(s)

def isSubsequence_dp(s, t):
    """
    time complexity: O(N)
    """
    dp = [[False] * (len(t)+1) for i in range(len(s)+1)]
    for i in range(len(t) + 1):
        dp[0][i] = True

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] and s[i-1] == t[j-1]
            else:
                dp[i][j]= dp[i][j-1]
    return dp[-1][-1]

# s = "abc"
# t = "ahbgdc"
# print(isSubsequence(s,t))

# s = "axc"
# t = "ahbgdc"
# print(isSubsequence(s,t))