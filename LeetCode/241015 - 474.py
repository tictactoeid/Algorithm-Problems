# Ones and Zeroes
# Medium


class Solution:
    def count(self, word: str) -> (int, int):
        zeros = 0
        ones = 0
        for char in word:
            if char == "0":
                zeros += 1
            elif char == "1":
                ones += 1
        return zeros, ones

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs))]
        # dp[i][j][k]: strs[i]까지 고려, 남은 0 j개, 남은 1 k개

        zeros, ones = self.count(strs[0])

        if zeros <= m and ones <= n:
            dp[0][m - zeros][n - ones] = 1

        for i in range(1, len(strs)):
            zeros, ones = self.count(strs[i])
            for j in range(m + 1):
                for k in range(n + 1):
                    if j + zeros <= m and k + ones <= n:
                        dp[i][j][k] = max(dp[i - 1][j + zeros][k + ones] + 1, dp[i - 1][j][k])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                    # dp[i][j-zeros][k-ones] = dp[i-1][j][k] + 1
                    # => dp[i][j][k] = dp[i-1][j+zeros][k+ones] + 1
                    # or

                    # dp[i][j][k] = dp[i-1][j][k]

        answer = 0
        for j in range(m + 1):
            for k in range(n + 1):
                answer = max(answer, dp[-1][j][k])
        # print(dp)
        return answer
