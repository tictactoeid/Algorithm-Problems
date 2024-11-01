# Handshakes That Don't Cross
# Hard

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10 ** 9 + 7

        n = numPeople
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[2] = 1

        for i in range(4, n + 2, 2):
            for x in range(i - 2, -1, -2):
                dp[i] += (dp[x] * dp[i - 2 - x])
                dp[i] %= MOD

        # print(dp)
        return dp[n] % MOD
