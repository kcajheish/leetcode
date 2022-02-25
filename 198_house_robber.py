def rob_recursive(nums):
    """
    time complexity: O(N^2)
    space complexity: O(1)
    """
    def dp(nums, start):
        if start >= len(nums):
            return 0

        res = max(
            nums[start] + dp(nums, start+2),
            dp(nums, start+1)
        )
        return res
    return dp(nums, 0)

def robDPMemo(nums):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    memo = [-1] * len(nums)
    def dp(nums, start):

        # if no more house can be visit, return 0 price
        if start >= len(nums):
            return 0

        # if we have attempt rob houe from here, return immediately to save time
        if memo[start] != -1:
            return memo[start]

        # find the largest between two choices: rob or skip this house
        res = max(
            nums[start] + dp(nums, start+2),
            dp(nums, start+1)
        )

        # save the results for future lookup
        memo[start] = res

        return res
    return dp(nums, 0)

def rob_top_down_dp(nums):
    dp = [0] * (len(nums) + 2)
    for i in range(len(nums)-1, -1, -1):
        dp[i] = max(dp[i+2] + nums[i], dp[i+1])
    return dp[0]
