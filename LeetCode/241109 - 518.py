# Coin Change II
# Medium

class Solution:
    def dp(self, idx, amount):
        if amount < 0:
            return 0
        elif amount == 0:
            return 1
        elif idx >= self.n:
            return 0
        elif (idx, amount) in self.memo:
            return self.memo[(idx, amount)]

        else:
            coin = self.coins[idx]
            value = 0
            remain = amount
            while remain >= 0:
                value += self.dp(idx + 1, remain)
                remain -= coin

            self.memo[(idx, amount)] = value
            return value

    def change_recur(self, amount: int, coins: List[int]) -> int:
        # 중복처리 때문에 1차원 dp로 안 됨
        self.memo = {}
        self.coins = coins
        self.n = len(coins)

        value = self.dp(0, amount)
        # print(self.memo)
        return value

    def change(self, amount, coins):
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            coin = coins[i]
            for j in range(1, amount + 1):
                if j - coin >= 0:
                    dp[i][j] = dp[i][j - coin] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][amount]
