# Best Time to Buy and Sell Stock with Transaction Fee
# Medium

class Solution:
    def maxProfit_tle(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [0 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                # j에 사서 i에 판매
                profit = max(prices[i] - prices[j] - fee, 0)
                if j >= 1:
                    total = dp[j - 1] + profit
                else:
                    total = profit

                dp[i] = max(dp[i], dp[j], total)
                # dp[j]: j 이후로 팔거나 사지 않는 경우

        # print(dp)
        return dp[-1]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        # state: hold, reset
        # (buy) reset -> hold
        # (sell) hold -> reset
        # (stay) reset -> reset, hold -> hold
        n = len(prices)

        reset = 0
        hold = -math.inf

        for i in range(n):
            reset = max(reset, hold + prices[i] - fee)
            hold = max(hold, reset - prices[i])

        return max(reset, hold)
