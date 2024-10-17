# Distinct Subsequences
# Hard

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]: s[:i+1]의 subsequence로 t[:j+1]을 만들 수 있는 경우의 수

        dp = [[0 for _ in range(len(t))] for _ in range(len(s))]

        count = 0
        for idx, char in enumerate(s):
            if char == t[0]:
                count += 1
            dp[idx][0] = count

        # for i in range(len(s)+1):
        #     dp[i][0] = 1
        # dp[0] = [1 for _ in range(len(t)+1)]

        for i in range(1, len(s)):
            for j in range(1, len(t)):
                if s[i] == t[j]:
                    dp[i][j] = 0
                    dp[i][j] += dp[i - 1][j]  # exclude s[i]
                    dp[i][j] += dp[i - 1][j - 1]  # include s[i]
                else:
                    dp[i][j] = dp[i - 1][j]  # exclude s[i]

        # for j in range(1, len(t) + 1):
        #     count = 0
        #     for i in range(1, len(s) + 1):
        #         if s[i-1] == t[j-1]:
        #             count += 1
        #         dp[i][j] = count * dp[i-1][j-1]

        # for i in range(1, len(s)):
        #     for j in range(1, len(t)):
        #         if s[i] == t[j]:
        #             count += 1
        #             # TODO
        #             dp[i][j] += dp[i-1][j-1]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # print(dp)
        # return max(map(max, dp))
        return dp[-1][-1]

