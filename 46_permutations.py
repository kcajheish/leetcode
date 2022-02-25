"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.backtrack(nums, [], results)
        return results

    def backtrack(self, nums, subset, results):
        # if the number we have selected reach the length of nums, we find our solution
        if len(subset) == len(nums):
            results.append(list(subset))
            return

        # assume we are looking for our pick at i,
        # try out each in nums if it has not been picked before
        for num in nums:
            if num in subset:
                continue
            subset.append(num)

            # after backtrack return, the subset will be recovered to state before tracking
            # after this, continue to our next pick
            self.backtrack(nums, subset, results)
            subset.pop()

        return results

if __name__ == '__main__':
    s = Solution()
    results = s.permute([1,2,3])
    print(results)
