from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        time complexity O(n)
        space complexity O(n)

        arr is sorted.
        to find whether current element is duplicated, look one element before him
        """
        start = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[start] = nums[i]
                start += 1
        return start
