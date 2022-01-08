# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
:type: List[int]
:rtype: int
'''
# Solution 1

class Solution:
    def maxProfit(self, prices):
        local_minimum = prices[0]
        global_maximum = 0
        for price in prices:
            if price > local_minimum:
                profit = price - local_minimum
                global_maximum = max(profit, global_maximum)
            else:
                local_minimum = price
        return global_maximum

'''
time complexity: O(n) Only a single pass is needed.
space complexity: O(1) Only two variables are used.
'''

# Solution 2: Brute-force

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
'''
time complexity: O(n2). Loop runs \dfrac{n*(n-1)}{2} times.
space complexity: O(1). Only two variables - maxprofit and profit are used.
'''