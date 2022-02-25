from typing import List

class Solution:
    def removeElementPop(self, nums: List[int], val: int) -> int:
        """
        time complexity: O()

        idea:
        when evern an element is matched, pop the element and fix the left index.
        else, shit left index to the right
        """
        count = len(nums)
        l = 0
        while count > 0:
            if nums[l] == val:
                nums.pop(l)
            else:
                l += 1
            count -= 1
        return len(nums)

    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for num in nums:
            if num != val:
                nums[pointer] = num
                pointer += 1
        return pointer
