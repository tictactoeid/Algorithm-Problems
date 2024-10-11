# Regular Expression Matching
# Hard

# 어려운 dp 문제

class Solution:
    pattern = []

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        # dp[i][j] = if s[:i] matches p[:j]

        dp[0][0] = True  # "" matches ""
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # zero element matches

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                char = s[i - 1]
                pattern = p[j - 1]
                if pattern == '*':
                    dp[i][j] = dp[i][j] or dp[i][j - 2]  # zero element matches

                    if p[j - 2] == char or p[j - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # one or more element matches

                elif pattern == char or pattern == ".":
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]
