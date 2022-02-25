from collections import defaultdict
def lengthOfLongestSubstring(s):
    """
    time complexity: O(N)
    idea: max substring without repeating character -> sliding window
    use left as left bound of the window, right as right bound of window,
    inside the window, character should be unique
    """
    if s == '':
        return 0

    count = defaultdict(int)
    left, right = 0, 0
    largest_window = 0
    while right < len(s):
        right_char = s[right]
        count[right_char] += 1
        if count[right_char] == 1:
            largest_window = max(largest_window, right - left + 1)

        while count[right_char] > 1:
            left_char = s[left]
            count[left_char] -= 1
            left += 1

        right += 1

    return largest_window