# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
  
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        # Initialize profit to 0 since no transactions have been made yet
        profit = 0
        
        # Set the first element as the initial minimum price
        min_value = prices[0]
        
        # Initialize the index of the minimum price (for reference, though not used directly in the profit calculation)
        min_index = 0
        
        # Loop through each price in the list
        for i in range(len(prices)):
            
            # If the current price is lower than the previously recorded minimum price
            if prices[i] < min_value:
                # Update the minimum price to the current price
                min_value = prices[i]
                
                # Update the index of the minimum price
                min_index = i
            
            # Calculate the profit if the stock were sold on the current day
            # (subtracting the minimum price from the current price)
            # If this profit is greater than the current best profit, update the profit
            if prices[i] - prices[min_index] > profit:
                profit = prices[i] - prices[min_index]
        
        # Return the maximum profit found
        return profit
