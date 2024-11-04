# Minimum Path Sum
# Medium

class Solution:
    def minPathSum_Dijkstra(self, grid: List[List[int]]) -> int:
        # O(mn log mn)
        heap = []
        m = len(grid)
        n = len(grid[0])
        distance = [[math.inf for _ in range(n)] for _ in range(m)]

        x, y, dist = 0, 0, grid[0][0]
        distance[x][y] = dist
        heapq.heappush(heap, (dist, x, y))

        while heap:
            dist, x, y = heapq.heappop(heap)
            if dist > distance[x][y]:
                continue
            for i, j in [(x + 1, y), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n:
                    new_dist = dist + grid[i][j]
                    if new_dist < distance[i][j]:
                        distance[i][j] = new_dist
                        heapq.heappush(heap, (new_dist, i, j))

        return distance[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        # O(mn)
        m, n = len(grid), len(grid[0])

        dp = [[math.inf for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue

                up = dp[i - 1][j] if i > 0 else math.inf
                left = dp[i][j - 1] if j > 0 else math.inf
                dp[i][j] = min(up, left) + grid[i][j]

        return dp[-1][-1]
