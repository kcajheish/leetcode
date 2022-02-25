def rob_dp_bottom_up(nums):
    def _rob(nums, l, r):
        dp = [0] * (len(nums) + 2)
        for i in range(r, l-1, -1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        return dp[l]
    return max(
        _rob(nums, 0, len(nums)-2),
        _rob(nums, 1, len(nums)-1)
    )
def rob_dp_bottom_up_less_space(nums):
    def _rob(nums, l, r):
        current, previous = 0, 0
        for i in range(l, r + 1, 1):
            previous, current = current, max(previous+nums[i], current)
        return current
    return max(
        _rob(nums, 0, len(nums)-2),
        _rob(nums, 1, len(nums)-1)
    )
def rob_dp_top_down(nums):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    def dp(nums, l, end, memo):
        if l >= end:
            return 0
        if l in memo:
            return memo[l]
        res = max(
            dp(nums, l+2, end, memo) + nums[l],
            dp(nums, l+1, end, memo)
        )
        memo[l] = res
        return res
    return max(
        dp(nums, 0, len(nums)-2, {}),
        dp(nums, 1, len(nums)-1, {})
    )
# r = rob([2,3,2])
# print(r)