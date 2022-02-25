from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            product *= nums[i-1]
            res[i] *= product

        product = 1
        for j in range(len(nums)-2, -1, -1):
            product *= nums[j+1]
            res[j] *= product
        return res
