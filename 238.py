"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up:

Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        lp = 1
        for l in range(len(nums)):
            product.append(lp)
            lp = lp * nums[l]

        rp = 1
        for r in range(len(nums)-1, -1, -1):
            product[r] *= rp
            rp *= nums[r]

        return product

if __name__ == '__main__':
    s = Solution()
    arr = [1,2,3,4]
    expect = [24, 12, 8, 6]
    result = s.productExceptSelf(arr)
    assert expect == result
    print(f"result: {result}; expect: {expect}")
    print("test completed")