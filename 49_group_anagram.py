"""
group anagram
using counting sort, which give time complexity O(N)
** already knows the order of key e.g. z = 26, a = 1, ... and so on
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = self.counting_sort(s)
            groups[key].append(s)

        return list(groups.values())

    def counting_sort(self, s):
        counter = [0 for i in range(26)]
        for c in s:
            counter[ord(c) - ord('a')] += 1
        output = []
        for i in range(26):
            output.append(counter[i] * chr(i + ord('a')) )
        return ''.join(output)

def groupAnagrams(strs):
    """
    letters in same anagrams share same set and number of the characters
    simply sorted letters as key.
    if any two letters share the same key, they belongs to same anagrams
    """
    seen = defaultdict(list)
    for letters in strs:
        key = ''.join(sorted(letters))
        seen[key].append(letters)
    return [ seen[key] for key in seen]