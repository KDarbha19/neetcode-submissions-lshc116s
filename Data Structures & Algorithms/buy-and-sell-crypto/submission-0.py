class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        amount = 0
        for i in range(len(prices)):
            if max(prices[i:len(prices)]) == prices[i]:
                amount = max(amount, 0)
            else:
                temp = max(prices[i + 1:len(prices)]) - prices[i]
                amount = max(amount, temp)
        return amount 

        