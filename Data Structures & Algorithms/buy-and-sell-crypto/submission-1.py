class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 #Initial result 

        for i in range(len(prices)): # Left window ready
            buy = prices[i] #Left window buys
            for j in range(i + 1, len(prices)): # Right window after left stopping at end of array
                sell = prices[j] # sell price is set 
                result = max(result, sell - buy) # max set pick the higher result 
        return result #return result 