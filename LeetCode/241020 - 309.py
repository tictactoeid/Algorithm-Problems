# Best Time to Buy and Sell Stock with Cooldown
# Medium

class Solution:
    def maxProfit_dp(self, prices: List[int]) -> int:

        # dp[i][j]: i일까지 지났을 때의 최댓값, 단 j일에 팔았을 때. (즉 j+1일이 cooldown)

        n = len(prices)

        dp = [0] * n

        if n > 1:
            dp[1] = max(0, prices[1] - prices[0])

        for i in range(2, n):
            sell = 0
            for j in range(i):
                profit = prices[i] - prices[j]
                if j >= 2:
                    profit += dp[j - 2]
                sell = max(profit, sell)
            dp[i] = max(dp[i - 1], sell)

        return dp[-1]

    def maxProfit_state(self, prices: List[int]) -> int:
        # State Machine Approach
        # States: held, sold, reset

        # buy: reset -> held
        # held: held -> held
        # sold: held -> sold
        # cooldown: sold -> reset
        # rest: reset -> reset

        n = len(prices)

        sold = [-math.inf for _ in range(n + 1)]
        held = [-math.inf for _ in range(n + 1)]
        reset = [0 for _ in range(n + 1)]

        # sold[i]: prices[i-1]의 시점

        for i in range(1, n + 1):
            price = prices[i - 1]
            held[i] = max(held[i - 1], reset[i - 1] - prices[i - 1])
            reset[i] = max(reset[i - 1], sold[i - 1])
            sold[i] = held[i - 1] + prices[i - 1]

        print(held)
        print(reset)
        print(sold)
        return max(sold[n], reset[n])

    def maxProfit(self, prices: List[int]) -> int:
        # State Machine Approach with O(1) space

        sold = -math.inf
        held = -math.inf
        reset = 0

        n = len(prices)

        for i in range(n):
            price = prices[i]
            held_before = held
            held = max(held_before, reset - price)
            reset = max(reset, sold)
            sold = held_before + price

        return max(sold, reset)
    