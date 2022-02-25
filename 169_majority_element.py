"""
http://users.ece.northwestern.edu/~dda902/336/hw4-sol.pdf
"""

def majorityElemen_hash(nums):
    """
    hashtable, space O(N) time(N)
    """
    count = dict()
    size = len(nums)
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1

        if count[num] > size/2:
            return num
    return -1


def majorityElement_divide_and_conquer(nums):
    def get_majority(nums, l, r):
        if l == r:
            return nums[l]

        mid = l + (r-l)//2
        left_most = get_majority(nums, l, mid)
        right_most = get_majority(nums, mid+1, r)
        if left_most == right_most:
            return left_most

        left_count = get_frequency(nums,l, r,left_most)
        right_count = get_frequency(nums,l, r, right_most)
        half = (r - l + 1)/2
        # print(f"left {l}, mid {mid}, right {r}",nums[l:r+1] )
        # print(f"{left_most}, {right_most}")
        if left_count > half:
            return left_most
        elif right_count > half:
            return right_most
        return 'NOT-FOUND'

    def get_frequency(nums, l, r, val):
        if val == 'NOT-FOUND':
            return 0
        f = 0
        for num in nums[l:r+1]:
            if num == val:
                f += 1
        return f
    return get_majority(nums, 0, len(nums)-1)

def majorityElement_sort(nums):
    nums.sort()
    return nums[len(nums)//2+1]

def majorityElement_moore_voting(nums):
    major = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == major:
            count += 1
        elif count:
            count -= 1
        else:
            major = nums[i]
            count = 1
    return major

# majorityElement = majorityElement_divide_and_conquer

# r = majorityElement([3,2,3])
# print(r)
