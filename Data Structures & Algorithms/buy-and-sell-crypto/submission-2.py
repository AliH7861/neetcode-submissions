class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        maxValue = 0

        for right in range(0, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxValue = max(maxValue, profit)

        return maxValue
