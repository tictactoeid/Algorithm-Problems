# Swim in Rising Water
# Hard


class Solution:
    def swimInWater_Dijkstra(self, grid: List[List[int]]) -> int:
        # O(n^2 logn) Dijkstra's Soln
        heap = []
        n = len(grid)
        distance = [[math.inf for _ in range(n)] for _ in range(n)]

        distance[0][0] = grid[0][0]

        heapq.heappush(heap, (distance[0][0], 0, 0))

        while heap:  # O(n^2): each cell processed once
            dist, r, c = heapq.heappop(heap)  # O(logn)
            if distance[r][c] < dist:
                continue

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # O(1)
                if 0 <= x < n and 0 <= y < n:
                    next_dist = max(dist, grid[x][y])
                    if next_dist < distance[x][y]:
                        distance[x][y] = next_dist
                        heapq.heappush(heap, (next_dist, x, y))  # O(logn)

        # print(distance)
        return distance[-1][-1]

    def swimInWater_bfs(self, grid: List[List[int]]) -> int:
        # O(n^2 logn) BFS + heap soln
        # heap을 사용하는 특성상 Dijkstra's랑 구현에 큰 차이가 없는듯?
        # distance를 저장하는지 visited를 저장하는지만 차이

        q = []
        n = len(grid)

        if n == 1:
            return grid[0][0]

        visited = [[False for _ in range(n)] for _ in range(n)]

        visited[0][0] = True
        heapq.heappush(q, (grid[0][0], 0, 0))

        while q:
            dist, r, c = heapq.heappop(q)
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < n and 0 <= y < n:
                    if not visited[x][y]:
                        next_dist = max(dist, grid[x][y])
                        heapq.heappush(q, (next_dist, x, y))
                        visited[x][y] = True
                    if (x, y) == (n - 1, n - 1):
                        return next_dist

    def find(self, i1, j1):
        if self.parents[i1][j1] != (i1, j1):
            parent = self.parents[i1][j1]
            self.parents[i1][j1] = self.find(parent[0], parent[1])
        return self.parents[i1][j1]

    def union(self, i1, j1, i2, j2):
        p1 = self.find(i1, j1)
        p2 = self.find(i2, j2)
        if p1 == p2:
            return

        if self.grid[p1[0]][p1[1]] > self.grid[p2[0]][p2[1]]:
            self.parents[p2[0]][p2[1]] = p1
        else:
            self.parents[p1[0]][p1[1]] = p2

    def swimInWater(self, grid: List[List[int]]) -> int:
        # Union-Find
        # grid의 각 원소가 0부터 n^2 - 1이 1번씩만 등장하기 때문에,
        # i = 0, 1, 2, ... n^2 - 1까지 차례로
        # i의 neighbor 중 본인보다 작은 것과 union
        # grid[0][0]과 grid[-1][-1]이 union된 순간의 i가 정답

        n = len(grid)
        index = [(-1, -1) for _ in range(n ** 2)]

        self.parents = [[(i, j) for j in range(n)] for i in range(n)]
        self.grid = grid

        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                index[x] = (i, j)
        for i in range(n ** 2):
            r, c = index[i]
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] < i:
                    self.union(r, c, x, y)
            # print(self.parents)
            if self.find(0, 0) == self.find(n - 1, n - 1):
                return i

        return 0
