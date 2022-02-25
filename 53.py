"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""
from typing import List

class Solution:
    def maxSubArray_v1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i-1]+num, num)
        return max(dp)

    def maxSubArray_v2(self, nums: List[int]) -> int:
        """
        in v1, max function in python costs too much runtime
        """
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if current_sum + num > current_sum:
                current_sum += num
            else:
                current_sum = num

            if current_sum > max_sum:
                max_sum = current_sum

if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert s.maxSubArray(nums) == 6
    nums = [1]
    assert s.maxSubArray(nums) == 1
    nums = [5,4,-1,7,8]
    assert s.maxSubArray(nums) == 23