from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.generate(n, 0, 0, [], results)
        return results

    def generate(self, n, left, right, subset, results):
        """
        idea: build parenthesis from ground up

        select either left and righ parenthesis each time to build the next character.
        when adding up, make sure parenthesises are balanced.
        when there are n pairs of parrenthesis in subset, we have solutions.
        """
        if left + right == 2*n:
            results.append(''.join(subset))

        if left < n:
            subset.append('(')
            self.generate(n, left+1, right, subset, results)
            subset.pop()

        if right < left:
            subset.append(')')
            self.generate(n, left, right+1, subset, results)
            subset.pop()

s = Solution()
r = s.generateParenthesis(3)
