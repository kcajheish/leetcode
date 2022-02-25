def prefixSum(nums):
    """
    store sum of first i elements in i index in array
    """
    sum_arr = []
    current = 0
    for num in nums:
        current += num
        sum_arr.append(current)
    return sum_arr

def query(sum_arr, i, j):
    return sum_arr[j] - sum_arr[i-1]


class BinaryIndexTree:
    # less space than segment tree
    def __init__(self, arr):
        self.tree = [0] * len(arr)

