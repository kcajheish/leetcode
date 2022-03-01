def find_max_amplitude(arr, k)
    width = len(arr)
    max_stack = []
    min_stack = []
    arr = arr + arr
    amp = float('-inf')
    for i in range(width*2-k):
        while max_stack and arr[max_stack[-1]] < arr[i]:
            max_stack.pop()

        max_stack.append(i)

        while max_stack[0] <= i - (width-k) -1:
            max_stack.pop(0)

        while min_stack and arr[min_stack[-1]] > arr[i]:
            min_stack.pop()

        min_stack.append(i)

        while min_stack[0] <= i - (width-k):
            min_stack.pop(0)

        if i >= width - k:
            amp = max(arr[max_stack[0]]-arr[min_stack[0]], amp)
    return amp