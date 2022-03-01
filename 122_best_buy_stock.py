from typing import List
class Solution:
    """
    given prices, buy and sell stock
    prices = [7, 4, 2, 1]

    buy with least price
    sell with biggest price
    we are greedy when making choice of buying and selling
    """
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0
        for price in prices:
            if price > buy:
                sell += price - buy
                buy = price
            else:
                buy = price
        return sell