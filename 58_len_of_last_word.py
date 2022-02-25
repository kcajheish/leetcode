class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first = len(s) -1
        last = len(s) -1
        while s[first] == ' ' and first >= 0:
            first -= 1
        last = first

        while s[last] != ' ' and last >= 0:
            last -= 1
        return first - last


    def v1(self, s):
        length = 0
        for i in range(-1, -1-len(s), -1):
            c = s[i]
            if c != ' ':
                length += 1
            elif length > 0:
                break
        return length