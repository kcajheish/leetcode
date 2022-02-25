"""
given string s, return longest length where count of every character in subarray is above k
"""
from collections import defaultdict
def longestSubstring(s, k):
    """
    brute force, time complexity O(N^3)
    """
    longest = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring = s[i:j+1]
            count = defaultdict(int)
            char_over_k = 0
            for char in substring:
                count[char] += 1
                if count[char] == k:
                    char_over_k += 1
            if char_over_k == len(count):
                largest = max(largest, len(substring))
    return longest

def longestSubstring(s, k):
    """
    sliding window
        time complexity: O(N)
    """
    if not s or len(s) < k:
        return 0

    max_repeat_alphabet = 26
    largest = 0
    for target in range(1,max_repeat_alphabet):
        left, right = 0, 0
        number_of_alphabet = 0
        count = defaultdict(int)
        number_over_k = 0
        while right < len(s):
            if number_of_alphabet <= target:
                char = s[right]
                count[char] += 1
                if count[char] == k:
                    number_over_k += 1
                if count[char] == 1:
                    number_of_alphabet += 1
                right += 1
            else:
                while number_of_alphabet > target:
                    char = s[left]
                    count[char] -= 1
                    if count[char] == k - 1:
                        number_over_k -= 1
                    if count[char] == 0:
                        number_of_alphabet -= 1
                    left += 1
            if number_of_alphabet == number_over_k:
                window = right - left
                largest = max(largest, window)

    return largest


r1 = longestSubstring('assdflllkkjjnwe', 3)
r2 = longestSubstring('assdflllkkjjnwe', 2)
r3 = longestSubstring('assdflllkkjjnwe',1)
r4 = longestSubstring('cc', 3)

assert r1 == 3
assert r2 == 7
assert r3 == len('assdflllkkjjnwe')
assert r4 == 0
