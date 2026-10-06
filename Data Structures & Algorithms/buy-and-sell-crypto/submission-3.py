class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i, j = 0, len(prices)-1

        max_payout = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                diff  = sell - buy
                max_payout = max(max_payout, diff)
        return max_payout