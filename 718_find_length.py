def findLength(nums1, nums2):
    W = len(nums2)
    H = len(nums1)
    dp = [[0]*(W+1) for i in range(H+1)]
    res = 0

    for j in range(1,H+1):
        for i in range(1, W+1):
            if nums1[j-1] == nums2[i-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = 0
        res = max(res, dp[j][0])
    return res