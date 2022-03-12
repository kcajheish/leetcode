from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in '+-/*':
                stack.append(int(char))
            else:
                b, a = stack.pop(), stack.pop()
                res = None
                if char == '/':
                    res = int(a/b)
                elif char == '*':
                    res = a*b
                elif char == '+':
                    res = a+b
                elif char == '-':
                    res = a-b
                stack.append(res)
        return stack.pop()

s = Solution()
r = s.evalRPN(["4","13","5","/","+"])
r2 = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
assert r == 6
assert r2 == 22


