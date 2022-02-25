"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        r = x
        l = 0
        while l <= r:
            mid = l + (r - l)//2
            square = mid * mid
            if square <= x:
                l = mid + 1
                sqr = mid
            else:
                r = mid - 1
        return sqr

x = 8
expect = 2
s = Solution()
result = s.mySqrt(x)
print(result)
