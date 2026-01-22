# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        buy = prices[0]
        for i in prices[1:]:
            if i < buy:
                buy = i
            elif i - buy > max_diff:
                max_diff = i - buy
        
        return max_diff
