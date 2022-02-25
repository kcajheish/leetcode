def pancakeSort(arr):
    """
    time complexity
    """
    def swap(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    def sort(arr, n, results):
        if n == 0:
            return
        largest = 0
        for i in range(n):
            if arr[largest] < arr[i]:
                largest = i
        swap(arr, 0, largest)
        swap(arr, 0, n-1)
        results.append(largest+1)
        results.append(n)
        sort(arr, n-1, results)
    results = []
    sort(arr, len(arr), results)
    return results