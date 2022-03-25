import string
class Solution:
    """
    better implementation, check:
    https://leetcode.com/problems/decode-ways/discuss/1410794/C%2B%2BPython-From-Top-down-DP-to-Bottom-up-DP-O(1)-Space-Clean-and-Concise
    """
    def numDecodings(self, s: str) -> int:
        upper_cases = string.ascii_uppercase
        decode = {str(i+1): upper_cases[i] for i in range(26)}
        return self.count_decode(s, decode, {})

    def count_decode(self, s, decode, dp):
        if s in dp:
            return dp[s]

        count = 0
        for i in range(len(s)):
            sub = s[0:i+1]
            if sub in decode:
                if len(s) == len(sub):
                    count += 1
                count += self.count_decode(s[i+1:], decode, dp)
        dp[s] = count
        return dp[s]


s = Solution()
test_a = '9999'
expect_a = 1
assert s.numDecodings(test_a) == expect_a

test_b = '0001'
expect_b = 0
assert s.numDecodings(test_b) == expect_b

test_c = '10001'
expect_c = 0
assert s.numDecodings(test_c) == expect_c

test_d = '48205'
expect_d = 1
assert s.numDecodings(test_d) == expect_d

test_e = "11111111111111111111111111111111111111111"
s.numDecodings(test_e)