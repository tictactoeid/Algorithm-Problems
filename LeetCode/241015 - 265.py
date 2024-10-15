# Paint House II
# Hard

# Follow up: solve it in O(nk)
# O(nk^2)인 이유는 loop가 O(nk), loop 안에서 최솟값 찾는 데 O(k)
# 최솟값을 매번 찾지 않고 O(k)로 1번만 구해 놓으면 총 O(nk)로 풀 수 있다

class Solution:
    def get_minimun_indices(self, dp: List[int]) -> (int, int):
        first_min = 0
        second_min = 1
        if dp[0] > dp[1]:
            first_min = 1
            second_min = 0

        for i in range(2, len(dp)):
            if dp[first_min] > dp[i]:
                second_min = first_min
                first_min = i
            elif dp[second_min] > dp[i]:
                second_min = i

        # print(dp, first_min, second_min)
        return first_min, second_min

    def minCostII(self, costs: List[List[int]]) -> int:
        # O(nk)
        k = len(costs[0])
        n = len(costs)

        dp = [[0 for _ in range(k)] for _ in range(n)]
        dp[0] = costs[0]

        for i in range(1, n):  # O(n)
            first_min, second_min = self.get_minimun_indices(dp[i - 1])  # O(k)
            for j in range(k):  # O(k)
                if j == first_min:
                    dp[i][j] = costs[i][j] + dp[i - 1][second_min]
                else:
                    dp[i][j] = costs[i][j] + dp[i - 1][first_min]
                # dp[i][j] = costs[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])
        # print(dp)
        return min(dp[n - 1])

    def minCostII_nk2(self, costs: List[List[int]]) -> int:
        # O(nk^2)
        k = len(costs[0])
        n = len(costs)

        dp = [[0 for _ in range(k)] for _ in range(n)]

        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[i][j] = costs[i][j]
                else:
                    dp[i][j] = costs[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])

        return min(dp[n - 1])
