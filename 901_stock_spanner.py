class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        res = 1
        while len(self.stack) and self.stack[-1][1] <= price:
            span, some_price = self.stack.pop()
            res += span
        self.stack.append((res, price))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)