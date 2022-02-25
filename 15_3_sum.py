class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
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
    def threeSum(self, nums):
        pass

    def two_pointer(self, nums):
        """
        time complexity O(N^2)
        """
        nums.sort()
        _set = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            head = i
            start = i + 1
            end = len(nums) -1
            while start < end:
                s = nums[head] + nums[start] + nums[end]
                if s == 0:
                    _set.add((nums[head], nums[start], nums[end]))
                    start += 1
                elif s > 0:
                    end -= 1
                else:
                    start += 1
        return list(_set)
