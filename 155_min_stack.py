class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        least = val if not self.stack else self.getMin()
        self.stack.append((val, min(val, least)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

