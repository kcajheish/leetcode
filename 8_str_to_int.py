class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = 2**31-1, -2**31
        start = 0

        while len(s) > start and s[start] == ' ':
            start += 1

        if start == len(s):
            return 0

        first_letter = s[start]

        sign = -1 if first_letter == '-' else 1
        if first_letter in {'+', '-'}:
            start += 1

        end = start
        while end < len(s) and s[end].isdigit():
            end += 1

        if start == end:
            return 0

        value = int(s[start:end]) * sign
        if value < MIN:
            return MIN
        elif value > MAX:
            return MAX
        else:
            return value
        return int(s[start:end]) * sig

    def myAtoi(self, s):
        """
        approach the problem by adding up integer on demand
        """
        pass