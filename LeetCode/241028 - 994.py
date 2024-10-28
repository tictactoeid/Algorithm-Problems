# Rotting Oranges
# Medium

class Solution:
    def elapse_one(self, grid: List[List[int]], fresh_count: int) -> (List[List[int]], int):
        if fresh_count == 0:
            return fresh_count

        m = len(grid)
        n = len(grid[0])
        next_grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    next_grid[i][j] = grid[i][j]
                else:  # grid[i][j] == 1
                    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                    for x, y in neighbors:
                        if 0 <= x < m and 0 <= y < n:
                            if grid[x][y] == 2:
                                next_grid[i][j] = 2
                                fresh_count -= 1
                                break
                    if next_grid[i][j] != 2:
                        next_grid[i][j] = 1

        # print(next_grid, fresh_count)
        return next_grid, fresh_count

    def orangesRotting_simulate(self, grid: List[List[int]]) -> int:
        # simulate
        m = len(grid)
        n = len(grid[0])

        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
        # print(fresh_count)
        time = 0
        while fresh_count > 0:
            next_grid, next_count = self.elapse_one(grid, fresh_count)
            if next_count != 0 and next_count == fresh_count:
                return -1
            time += 1
            grid = next_grid
            fresh_count = next_count
        return time

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        q = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        answer = 0
        while q:
            i, j, time = q.popleft()
            answer = max(time, answer)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1:
                        grid[x][y] = 2  # visited
                        q.append((x, y, time + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return answer



