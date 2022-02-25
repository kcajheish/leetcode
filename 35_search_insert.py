from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        time complexity: O(log n)
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l