# Maximal Square
# Medium

class Solution:
    def maximalSquare_1(self, matrix: List[List[str]]) -> int:
        # TC O(mn), SC O(mn)
        # col과 row의 prefix sum을 이용

        m = len(matrix)
        n = len(matrix[0])

        col_sum = [[0 for _ in range(n)] for _ in range(m)]
        row_sum = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                if j > 0:
                    row_sum[i][j] += row_sum[i][j - 1] + 1
                else:
                    row_sum[i][j] = 1
                if i > 0:
                    col_sum[i][j] += col_sum[i - 1][j] + 1
                else:
                    col_sum[i][j] = 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        answer = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == "1":
                        dp[i][j] = 1
                        answer = max(answer, dp[i][j])
                elif matrix[i][j] == "1":
                    dp[i][j] = max(1, min(dp[i - 1][j - 1] + 1, row_sum[i][j], col_sum[i][j]))
                    answer = max(answer, dp[i][j])

        return answer ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # TC, SC 모두 위와 동일
        # 더 깔끔한 풀이
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        answer = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                left = dp[i][j - 1] if j > 0 else 0
                right = dp[i - 1][j] if i > 0 else 0
                diag = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                dp[i][j] = min(left, right, diag) + 1
                answer = max(answer, dp[i][j])

        return answer ** 2
