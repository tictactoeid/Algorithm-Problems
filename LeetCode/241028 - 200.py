# Number of Islands
# Medium

class Solution:
    def bfs(self, i: int, j: int, num: int):
        if self.visited[i][j]:
            return

        q = deque()
        q.append((i, j))
        self.visited[i][j] = num

        while q:
            i, j = q.popleft()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < self.m and 0 <= y < self.n:
                    if not self.visited[x][y] and self.grid[x][y] == "1":
                        self.visited[x][y] = num
                        q.append((x, y))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        m = self.m
        n = self.n
        self.visited = [[0 for _ in range(n)] for _ in range(m)]

        num = 0
        for i in range(m):
            for j in range(n):
                if not self.visited[i][j] and self.grid[i][j] == "1":
                    num += 1
                    self.bfs(i, j, num)
                    # print(self.visited)

        return num
