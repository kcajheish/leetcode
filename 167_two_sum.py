def twoSum_two_pointer(numbers, target):
    """
    space complexity: O(1)
    time complexity: O(N)
    """
    l, r = 0, len(numbers)-1
    while l < r:
        two_sum = numbers[l] + numbers[r]
        if two_sum < target:
            l += 1
        elif two_sum > target:
            r -= 1
        else:
            break
    return [l+1, r+1]