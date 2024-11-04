# Longest Common Subsequence
# Medium

class Solution:
    def longestCommonSubsequence_dp(self, text1: str, text2: str) -> int:
        # TC: O(mn)
        # SC: O(mn)
        m, n = len(text1), len(text2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # TC: O(mn)
        # SC improved as O(m+n)
        # dp 배열 중 어차피 마지막 2개의 row만 사용한다는 것을 이용

        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)  # m >= n

        prev_row = [0] * (m + 1)
        curr_row = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr_row[j] = prev_row[j - 1] + 1
                else:
                    curr_row[j] = max(curr_row[j - 1], prev_row[j])
            prev_row = curr_row
            curr_row = [0] * (n + 1)

        return prev_row[-1]
