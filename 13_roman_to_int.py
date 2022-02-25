class Solution:
    def romanToInt(self, s: str) -> int:
        rule = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        neg_rule = {
            'I': {'V', 'X'},
            'X': {'L', 'C'},
            'C': {'D', 'M'}
        }

        number=0
        for i, c in enumerate(s):
            val = rule[c]
            if c in neg_rule and (i+1) < len(s):
                c_next = s[i+1]
                if c_next in neg_rule[c]:
                    val *= -1
            number += val

        return number