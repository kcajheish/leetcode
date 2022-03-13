from collections import defaultdict
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        observation:
        modify in place
        entry in nums has few value

        thought:
        to modify in-place, available sort is quick sort/bubble/counting sort
        since entry has few value, counting gives the best time and space complexity

        time complexity: O(n)
        space complexity: O(m), where m is number of available value
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        p = 0
        for color in [0, 1, 2]:
            for i in range(count[color]):
                nums[p] = color
                p += 1