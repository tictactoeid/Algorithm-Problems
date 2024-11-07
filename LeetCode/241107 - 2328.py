# Number of Increasing Paths in a Grid
# Hard

class Solution:
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        count = 1  # self

        for (x, y) in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < self.m and 0 <= y < self.n:
                if self.grid[x][y] > self.grid[i][j]:
                    count += self.dp(x, y)

        count %= (10 ** 9 + 7)
        self.memo[(i, j)] = count
        return count

    def countPaths(self, grid: List[List[int]]) -> int:
        # DFS with memoization
        # TC and SC: O(mn)

        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        self.memo = {}

        answer = 0
        for i in range(self.m):
            for j in range(self.n):
                answer += self.dp(i, j)
        # print(self.memo)
        return answer % (10 ** 9 + 7)
