def findErrorNums(nums):
    dup = -1
    mis = -1
    for j in range(nums):
        i = j + 1
        num = nums[i]
        if num < 0:
            dup = abs(num)
        nums[abs(num)] *=  -1

    for k in range(nums):
        if nums[k] > 0:
            mis = nums[k]
    return [dup, mis]
def brute_force(nums):
    """
    time: O(N)
    space: O(N) -> can it be improved?
    """
    dic = dict()
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    dup = -1
    mis = -1
    for i in range(1, len(nums)+1):
        if i not in dic:
            mis = i

        if dic[i] > 1:
            dup = i
    return [dup, mis]
