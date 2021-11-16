#!/usr/bin/env python3

from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        # Since I can buy and sell everyday, then I will calculate what's the everyday profit from the previous day.
        # Then I will just take the positive profite to maximize.
        #

        profits = ((prices[i] - prices[i-1]) for i in range(1, len(prices)))
        better_profits = filter(self.isPositive, profits)
        total_profit = sum(better_profits)

        return total_profit

    def isPositive(self, x):
        return True if x > 0 else False



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,5,15,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
