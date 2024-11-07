# Shortest Distance from All Buildings
# Hard

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # TC: O(m^2 n^2)
        # SC: O(mn)
        m, n = len(grid), len(grid[0])

        buildings = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))

        distance = [[0 for _ in range(n)] for _ in range(m)]
        # distance 배열에 각 building까지의 거리의 합을 모두 기록하고 최솟값을 return

        # print(buildings)
        for building in buildings:  # 최대 O(mn)
            q = deque()
            visited = [[False for _ in range(n)] for _ in range(m)]

            i, j = building
            visited[i][j] = True
            q.append((i, j, 0))

            while q:  # O(mn)
                i, j, dist = q.popleft()
                distance[i][j] += dist

                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if not visited[x][y] and (grid[x][y] == 0 or grid[x][y] == 3):
                            visited[x][y] = True
                            q.append((x, y, dist + 1))

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0 and not visited[i][j]:
                        grid[i][j] = 3
                        # 3: empty land이지만, 모든 building과 연결되어있지 않은 곳

        # print(distance)
        answer = math.inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    answer = min(answer, distance[i][j])

        if answer == math.inf:
            return -1
        return answer
