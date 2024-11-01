# Coin Change
# Medium

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            if coin < amount + 1:
                dp[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]
