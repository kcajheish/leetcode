"""
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sorted()
        i = 0
        j = 1
        k = len(nums) - 1
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)
            ref = nums[i] * -1

    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        """
        brute force o(n^3)
        """
        lookup = set()
        result = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                for k in range(j+1, len(nums), 1):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and (a, b, c) not in lookup:
                        result.append([a, b, c])
                        lookup.add((a,b,c))
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    expect = [[-1,-1,2],[-1,0,1]]
    result = s.threeSum(nums)
    print(f"expect: {expect}")
    print(f"result: {result}")

    assert result == expect
"""
排序 所以可能會有重複
"""