# Unique Paths II
# Medium

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                elif i >= 1 and j >= 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i >= 1:
                    dp[i][j] = dp[i-1][j]
                elif j >= 1:
                    dp[i][j] = dp[i][j-1]
                else:  # dp[0][0]
                    dp[i][j] = 1

        #print(dp)
        return dp[-1][-1]
