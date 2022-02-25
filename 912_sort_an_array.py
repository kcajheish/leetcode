"""
https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap
https://www.geeksforgeeks.org/quick-sort/
"""

def insertion_sort(nums):
    """
    time complexity: O(N^2)
    space complexity: O(N)
    """
    for i in range(len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    return nums

def bubble_sort(nums):
    """
    time complexity: O(N^2)
    space complexity: O(N) -> the size of the array
    """
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def selection_sort(nums):
    """
    time complexity: O(N^2) , quadratic
    space complexity: O(N)
    """
    def find_min(nums, l , r):
        least, pos = nums[l], l
        for i in range(l+1, r+1):
            if nums[i] < least:
                least = nums[i]
                pos = i
        return least, pos

    for i in range(len(nums)):
        least, pos = find_min(nums, i, len(nums)-1)
        nums[i], nums[pos] = least, nums[i]
    return nums

def merge_sort(nums):
    """
    time complexity: O(NlogN)
    space complexity: O(N)
    why space complexity of merge sort is not nlogn?
        ref: https://stackoverflow.com/a/28641693
    """
    if len(nums) == 1 :
        return nums
    l, r = 0, len(nums) - 1
    m = l + (r-l)//2

    L = merge_sort(nums[l:m+1])
    R = merge_sort(nums[m+1:r+1])

    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            nums[k] = R[j]
            j += 1
        else:
            nums[k] = L[i]
            i+= 1
        k += 1

    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1

    return nums[l:r+1]

def heap_sort(nums):
    """
    time comlexity: O(N)
        check this lecture when doubt Nln(N)
        https://www.youtube.com/watch?v=B7hVxCmfPtM&ab_channel=MITOpenCourseWare
    space complexity: O(N)
    """
    def heapify(nums, i, n):
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l < n and nums[largest] < nums[l]:
            largest = l
        if r < n and nums[largest] < nums[r]:
            largest = r

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, largest, n)

    for i in range(len(nums)//2+1, -1, -1):
        heapify(nums, i, len(nums))

    for i in range(len(nums)-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)
    return nums

def quick_sort(nums):
    """
    time complexity: best case O(NlnN); O(N^2)
    space complexity: O(N) -> in place, no memory allocation cost
    """
    def partition(nums,l, r):
        pivot = nums[r]
        while l < r:
            while nums[l] < pivot:
                l += 1
            while nums[r] > pivot:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return l

    def _quick_sort(nums, l, r):
        if l>=r:
            return
        pivot_point = partition(nums, l, r)
        _quick_sort(nums, l, pivot_point-1)
        _quick_sort(nums, pivot_point+1, r)

    _quick_sort(nums, 0, len(nums)-1)
    return nums

test1= [2,1,6,4,7]
