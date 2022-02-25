from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        r = self.mergeSort(str_nums, 0, len(str_nums)-1)
        return ''.join(r) if r[0] != '0' else '0'

    def mergeSort(self, nums, l, r):
        if l == r:
            return [nums[l]]

        mid = l + (r-l)//2
        left_arr = self.mergeSort(nums, l, mid)
        right_arr = self.mergeSort(nums, mid+1, r)
        return self.merge(left_arr, right_arr)

    def merge(self, left_arr, right_arr):
        res = []
        l, r = 0, 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] + right_arr[r] > right_arr[r] + left_arr[l]:
                res.append(left_arr[l])
                l += 1
            else:
                res.append(right_arr[r])
                r += 1

        res += left_arr[l:] or right_arr[r:]
        return res
