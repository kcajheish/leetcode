from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for num in nums:
            if num not in lookup:
                lookup.add(num)
            else:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1]
    assert s.containsDuplicate(nums) == True
    nums = [1,2,3,4]
    assert s.containsDuplicate(nums) == False
    nums = [1,1,1,3,3,4,3,2,4,2]
    assert s.containsDuplicate(nums) == True

    print("test completed")