# Maximum Value of K Coins From Piles
# Hard

# 힌트 어느 정도 보고 풂

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # 현황을 담은 길이 k의 list
        # ex) [0, 1, 1, 1, 0, 0, 1, 1], k = 8
        # 라고 하면, 1, 2, 3, 6, 7번 pile에서 하나씩 고른 상태.

        # state = [1, 2, 3, 4, 0] 이라고 하면 0번 pile에서 하나, 1번 pile에서 2개, ... 의 원소의 합이 됨

        # -> k를, n개의 pile에 잘 분배하는 것
        # knapsack?

        # dp[0][0] = sum(piles[0:k])
        # dp[0][1] = sum(piles[0:k-1])
        # ...

        n = len(piles)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]

        sum_of_piles = [[0 for _ in range(len(piles[i]) + 1)] for i in range(n)]
        # sum_of_piles[i][j]: i번째 pile에서, 동전을 위에서부터 j개 골랐을 때의 합, j==0이면 0개 골랐으므로 0

        for i in range(n):
            for j in range(1, len(piles[i]) + 1):
                sum_of_piles[i][j] = sum_of_piles[i][j - 1] + piles[i][j - 1]

        for i in range(min(len(piles[0]) + 1, k + 1)):
            dp[0][k - i] = sum_of_piles[0][i]

        # dp[i][w]: ith pile까지 고려하였을 때, w개의 coin이 남은 상태.

        # dp[i][w] = dp[i-1][w] + sum_of_piles[i][0]
        # dp[i-1][w+1] + sum_of_piles[i][1]
        # dp[i-1][w+2] + sum_of_piles[i][2] ...

        # O(nk)
        for i in range(1, n):  # O(n)
            for w in range(k + 1):  # w + j <= k => O(k)
                j = 0
                while w + j < len(dp[i]) and j < len(sum_of_piles[i]):  # handle out of range
                    dp[i][w] = max(dp[i - 1][w + j] + sum_of_piles[i][j], dp[i][w])
                    j += 1

        return dp[-1][0]


