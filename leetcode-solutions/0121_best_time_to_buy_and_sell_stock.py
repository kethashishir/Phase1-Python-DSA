# LeetCode 121: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Approach: Track min price and calculate max profit
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price          # best (cheapest) buy so far
            else:
                profit = price - min_price # sell today vs best buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit

# Example run
print(Solution().maxProfit([7,1,5,3,6,4]))  # Output: 5
print(Solution().maxProfit([7,6,4,3,1]))    # Output: 0
