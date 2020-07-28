"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:


Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

HIGH LEVEL:
  Since we're only permitted to buy only once, we need to find the lowest prices as we iterate through the array, this will give us a Time Complexity of O(n)
  since we have to go throught the entire array to check the lowest price...
  this is what you'll do:

  lowestPrice = INF
  maxProfit = 0

  traverse through the list and 
    update the lowest price if the current number is lower that the lowestPrice
    update profit from the max between the current profit and the difference between (prices[i] - lowestPrice)

  return maxProfit

     

"""

def maxProfit(prices):
    lowestPrice = float("inf")
    maxProfit = 0
    
    for i in range(len(prices)):
        lowestPrice = min(lowestPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - lowestPrice)
        
    return maxProfit


print(maxProfit([7,1,5,3,6,4]))