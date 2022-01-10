# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''
:type: List[int]
:rtype: int
'''

# Solution 1: find peak, valley
# total profit = sum(peak - valley)
[7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices):
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit

'''
time complexity: O(n)
space complexity: O(1)
'''
# Solution 2: 
class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        total_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                total_profit += prices[i + 1] - prices[i]
        return total_profit

'''
time complexity: O(n)
space complexity: O(1)
'''
if __name__ = "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))