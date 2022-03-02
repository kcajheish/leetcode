class Solution:
    def rotate(self, nums, k):
        """
        rotate array with extra memory
        time complexity: O(n)
        space complexity: O(n)

        how to rotate in place?
        """
        results = [None]*len(nums)
        for i, num in enumerate(nums):
            to_i = (i + k) % len(nums)
            results[to_i] = num
        return results

    def rotatev2(self, nums, k):
        """
        observation: after k rotation, elements between k~end are on the left, 1~k-1 are on the right
        thought: reverse whole array, reverse 1~k-1 and then reverse k~end
        """
        k = k % len(nums)

        if not nums or not k:
            return

        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        print(nums)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

s = Solution()
r = s.rotatev2([1,2,3,4,5,6,7], 3)