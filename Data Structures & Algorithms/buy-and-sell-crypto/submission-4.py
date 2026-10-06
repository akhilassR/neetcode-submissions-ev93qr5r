class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i, j = 0, len(prices)-1

        # max_payout = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         diff  = sell - buy
        #         max_payout = max(max_payout, diff)
        # return max_payout

        l, r = 0, 1
        max_payout = 0
        while l < r and r < len(prices):
            buy, sell = prices[l], prices[r]
            if buy < sell:
                max_payout = max(max_payout, sell - buy)
            else:
                l = r
            r += 1
        return max_payout