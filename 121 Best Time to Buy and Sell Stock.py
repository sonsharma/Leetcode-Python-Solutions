# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Brute force 
# T: O(n2), S: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        for i in range(len(prices)-1):
            temp = max(prices[i+1:]) - prices[i]
            maxDiff = max(maxDiff, temp)
        return maxDiff

# One pass
# T: O(n), S: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        min_so_far = float("inf")
        
        for i in range(len(prices)):
            min_so_far = min(prices[i], min_so_far)
            maxDiff = max(maxDiff, prices[i] - min_so_far)
        return maxDiff
