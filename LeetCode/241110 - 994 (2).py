# Rotting Oranges
# Medium

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    count += 1

        if not count:
            return 0

        answer = 0

        while q and count > 0:
            i, j, dist = q.popleft()

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if not visited[x][y] and grid[x][y] != 0:
                        visited[x][y] = True
                        q.append((x, y, dist + 1))
                        if grid[x][y] == 1:
                            answer = max(answer, dist + 1)
                            count -= 1

        if count > 0:
            return -1
        return answer
