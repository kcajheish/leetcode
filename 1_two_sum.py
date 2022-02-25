def twoSum_memo(nums, target):
    """
    use memo to rememnber number if it is not visited before.
    tranverse the nums and lookup difference in target.
    if we found the difference, that means we found the answer
    """
    memo = dict()
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff not in memo:
            memo[nums[i]] = i
        else:
            break
    return i, memo[target-nums[i]]

def twoSum_two_pointer(nums, target):
    """
    why two pointer
    sorted array
    pick two number from the array that meet target
    """
    array = []
    for i, num in enumerate(nums):
        array.append((num, i))
    array.sort(key=lambda entry: entry[0])

    l, r = 0, len(nums) - 1
    while l < r:
        two_sum = array[l][0] + array[r][0]
        if two_sum < target:
            l += 1
        elif two_sum > target:
            r -= 1
        else:
            break
    return [array[l][1], array[r][1]]