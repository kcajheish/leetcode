from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        largest = dict()
        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]

            # from stack, pop out element that is smaller than current element
            # next larger will remains at top after this
            while stack and stack[-1] < num:
                stack.pop()

            if stack:
                # peek top element
                largest[num] = stack[-1]
            else:
                largest[num] = -1
            stack.append(num)

        return [ largest[num] for num in nums1]