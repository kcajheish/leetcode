"""
given n, find trailing zero of factorial of n

1! = 1
2! = 2
3! =  6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40230
9! = 362880
10! = 3628800...

observation: to find trailing zeroes, find out all the product of 2 and 5.

https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52373/Simple-CC%2B%2B-Solution-(with-detailed-explaination)
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        thought:
        find out number of factor 5 each integer from 1 to n
        use memo to remember results

        problems:
        a lot of wasted calculation on number that are not factor of five

        time complexity: amortized O(n)
        """
        num_of_5 = 0
        for i in range(1, n+1):
            num_of_5 += self.factor(i, 5, {})
        return num_of_5

    def factor(self, n, f, memo):
        if n in memo:
            return memo[n]

        if n % f == 0:
            res = 1 + self.factor(n/f, f, memo)
        else:
            res = 0
        memo[n] = res
        return memo[n]

    def trailingZeroesv2(self, n):
        """
        thought:
        start with solution, assume we look for number that has factor of 5, 5*5, 5*5*5...
        time complexity: O(n)
        """
        factor = 5
        res = 0
        while factor <= n:
            res += n//factor
            factor *= 5
        return res
