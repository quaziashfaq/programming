#!/usr/bin/env python3

from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buying_price = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - min_buying_price
            if profit > max_profit:
                max_profit = profit
            if price < min_buying_price:
                min_buying_price = price

        return max_profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,5,15,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
