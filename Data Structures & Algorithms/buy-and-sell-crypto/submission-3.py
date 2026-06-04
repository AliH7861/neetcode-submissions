class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Do get max profit you want to find lowest price to invest

        # Then sale at maximum value

        # So you need two values to be updated min and max

        left = 0
        maxVal = 0
      

        for right in range (1, len(prices)):
            
            # So condtion
            # If the following (right) is less then left = right
            if prices[right] < prices[left]:
                left = right

            profit = prices[right] - prices[left]
            maxVal = max(profit, maxVal)

        
        return maxVal


            


            
            
        
        

            
        