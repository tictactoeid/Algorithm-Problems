# Perfect Squares
# Medium

import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf for _ in range(n + 1)]

        i = 1
        while i ** 2 <= n:
            dp[i ** 2] = 1
            i += 1

        for i in range(1, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1

        return dp[n]
