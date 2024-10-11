# Wildcard Matching
# Hard

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            pattern = p[j - 1]
            if pattern == '*':  # empty sequence
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                char = s[i - 1]
                pattern = p[j - 1]

                if char == pattern or pattern == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        # print(dp)
        return dp[-1][-1]
