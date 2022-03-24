import unittest

class SlidingWindowMin:
    def sliding_min(self, nums, window):
        stack = []
        res = []
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                stack.pop()

            stack.append(i)

            while stack and stack[0] <= i - window:
                stack.pop(0)

            if i >= window -1:
                res.append(nums[stack[0]])
        return res

sw = SlidingWindowMin()
assert sw.sliding_min([4,3,0,3,1,6], 3) == [0, 0, 0, 1]
assert sw.sliding_min([4,3,2,1,0],2) == [3,2,1,0]
assert sw.sliding_min([1,2,3,4,5,6], 2) == [1,2,3,4,5]

class SubarraySum:
    def sum(self, nums, target):
        left, right = 0, 0
        total = 0
        while total != target and left < len(nums) and right < len(nums):
            if total < target:
                total += nums[right]
                right += 1
            elif total > target:
                total -= nums[left]
                left += 1
        if total == target:
            return left, right-1
        return -1, -1

ss = SubarraySum()
assert ss.sum([1,3,2,5,1,1,2,3], 8) == (2,4)
assert ss.sum([1,1,1,1], 5) == (-1, -1)
assert ss.sum([1,1,1,2,10], 6) == (-1, -1)

class TwoSum:
    def two_pointer(self, nums, target):
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right += 1
            else:
                break

        if left >= right:
            return -1, -1
        return nums[left], nums[right]

    def binary_search(self, nums, target):
        nums.sort()
        end = len(nums)-1
        for head in range(len(nums)):
            left, right = head+1, end
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid]+nums[head] > target:
                    right = mid-1
                elif nums[mid]+nums[head] < target:
                    left = mid+1
                else:
                    return nums[head], nums[mid]
        return -1, -1

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.two_sum = TwoSum()

    def test_order_nums(self):
        order_nums = [1,2,3,4,5,6]
        target = 9
        expect = 3, 6
        actual_two_pointer = self.two_sum.two_pointer(order_nums, target)
        actual_binary = self.two_sum.binary_search(order_nums, target)
        self.assertEqual(actual_two_pointer, expect)
        self.assertEqual(actual_binary, expect)

    def test_empty(self):
        nums = []
        actual_binary = self.two_sum.binary_search(nums, 8)
        actual_two_pointer = self.two_sum.two_pointer(nums, 8)
        self.assertEqual(actual_binary, (-1, -1))
        self.assertEqual(actual_two_pointer, (-1, -1))

    def test_repeat(self):
        nums = [3,2,2,2,5]
        actual_binary = self.two_sum.binary_search(nums, 7)
        actual_two_pointer = self.two_sum.two_pointer(nums, 7)
        self.assertEqual(actual_binary, (2, 5))
        self.assertEqual(actual_two_pointer, (2, 5))

class NearestSmaller:
    def small(self, nums):
        stack = []
        res = []
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            if not stack:
                res.append(None)
            else:
                res.append(stack[-1])
            stack.append(num)
        return res

class TestNearestSmaller(unittest.TestCase):
    def setUp(self):
        self.small = NearestSmaller().small

    def test_empty(self):
        self.assertEqual(self.small([]), [])

    def test_flat_num(self):
        test = [1,1,1,1,1,1]
        self.assertEqual(self.small(test), [None,None,None,None,None,None])

    def test_increasing(self):
        test = [1,2,3,4,5,6]
        self.assertEqual(self.small(test), [None,1,2,3,4,5])

    def test_decreasing(self):
        test = [6,5,4,3,2,1]
        self.assertEqual(self.small(test), [None,None,None,None,None,None])

    def test_edge(self):
        test = [1,6,5,4,3,2]
        self.assertEqual(self.small(test), [None,1,1,1,1,1])

if __name__ == '__main__':
    unittest.main()