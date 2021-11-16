#!/usr/bin/env python3

from typing import *

'''
Took help from this page
https://anj910.medium.com/leetcode-309-best-time-to-buy-and-sell-stock-with-cooldown-6bb794175ee2

We will consider three different actions for each day. We will consider the different profits
if we buy, sell, or cooldown on Day i. We will use 3 arrays to track all the possible max profits if our last action is to buy, sell, or cooldown TILL Day i.

 We always need to be careful about what action we took TILL Day (i-1) if we choose to do certain actions ON Day i.
We always need to check if we decide to buy/sell/cooldown today, can we earn more profit than yesterday,
if not, we will give up and remain the max profit we met so far.

In the buy/sell/cooldown array, we will separately record its max profit we can get so far with the condition that the last action is to buy/sell/cooldown.
Three cases needed to be considered on Day i:
1. If we decide to buy today, that means the last action till yesterday MUST BE cooldown since we cannot buy right after sell.
Then, we need to compare two profits: “if we cooldown yesterday and buy today” vs. “the max profit yesterday when the last action is to buy”.

2. If we decide to sell today, that means the last action till yesterday MUST BE buy since we need to buy if we want to sell.
Then we compare two profits: “if we sell the stock based on our last buy” vs. “the max profit yesterday when the last action is to sell”.

3. If we decide to cool down today, that means the last action till yesterday MUST BE sell OR cooldown.
We compare two profits: “the max profit yesterday when the last action is to sell” vs. “the max profit yesterday when the last action is cooldown”.

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #

        buy = [0 for i in range(n)]
        sell = [0 for i in range(n)]
        cooldown = [0 for i in range(n)]

        buy[0] = -prices[0]
        #print(buy, sell, cooldown)
        for i in range(1, n):
            buy[i] = max(buy[i-1], (cooldown[i-1] - prices[i]))
            sell[i] = max(sell[i-1], (buy[i-1] + prices[i]))
            cooldown[i] = max(cooldown[i-1], sell[i-1])
        #    print(buy, sell, cooldown)

        return max(sell[n-1], cooldown[n-1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,5,15,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([1,2,3,0,2]))
    print(s.maxProfit([1,2,5,0,2]))
    print(s.maxProfit([1,2,3,0,2,10]))
    print(s.maxProfit([1,2,5,0,2,10]))


# [1,2,3,0,2]
# [7,1,5,3,6,4]
# [7,5,15,1,5,3,6,4]
# [7,6,4,3,1]
# [1,2,5,0,2]
# [1,2,3,0,2,10]
# [1,2,5,0,2,10]

# Output
# 3
# 4
# 13
# 0
# 4
# 11
# 12



# 3
# 5
# 13
# 0
# 4
# 11
# 12
