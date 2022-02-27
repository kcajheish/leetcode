class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        digits = []
        x = abs(x)
        while x > 0:
            remain = x % 10
            if len(digits) or remain > 0:
                digits.append(remain)
            x = x // 10

        total = 0
        for i in range(len(digits)):
            total = total * 10 + digits[i]

        return 0 if total > pow(2,31) else total * sign

    def reverseV2(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        results = 0
        while x > 0:
            remain = x % 10
            results = results * 10 + remain
            x = x // 10

        return 0 if results > pow(2,31) else results * sign