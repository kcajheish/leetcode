"""
min sub array length
https://leetcode.com/problems/minimum-size-subarray-sum/
"""

def minSubArrayLen(nums, target):
    l, r, total, window = 0, 0, 0, float('inf')
    while r < len(nums):
        total += nums[r]
        while total >= target:
            window = min(window, r-l+1)
            total -= nums[l]
            l += 1
        r += 1
    return window if window < float('inf') else 0