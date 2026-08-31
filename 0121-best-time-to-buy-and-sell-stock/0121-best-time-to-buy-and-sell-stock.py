# Brute force
# O(n2)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)

        # i is the buying day
        for i in range(n-1):

            # j is the future selling day
            for j in range(i+1, n):
                currProfit = prices[j] - prices[i]
                maxProfit = max(currProfit, maxProfit)
        
        return maxProfit
'''


# Two pointer approach / Sliding window approach
# O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buying day, r = selling day
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            # If selling price is higher, calculate the profit
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)

            # Found a lower price, so use it as the new buying price
            else:
                l = r

            # Move to the next selling day
            r += 1

        return maxProfit



'''
# O(n)
# Main Logic:
# Keep track of the minimum stock price seen so far.
# For each day, calculate the profit if we sell at the current price.
# Update the maximum profit whenever a better profit is found.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Minimum price seen so far (best price to buy)
        minPrice = prices[0]

        maxProfit = 0

        for currPrice in prices:
            # Update the minimum buying price
            minPrice = min(currPrice, minPrice)

            # Calculate profit if we sell at the current price
            currProfit = currPrice - minPrice

            maxProfit = max(currProfit, maxProfit)

        return maxProfit
'''


