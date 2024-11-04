# Path With Minimum Effort
# Medium

class Solution:
    def is_reachable(self, heights, max_effort) -> bool:
        q = deque()
        m = len(heights)
        n = len(heights[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        q.append((0, 0))
        visited[0][0] = True
        while q:
            i, j = q.popleft()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if not visited[x][y] and abs(heights[x][y] - heights[i][j]) <= max_effort:
                        visited[x][y] = True
                        q.append((x, y))
                        if x == m - 1 and y == n - 1:
                            return True

        return visited[-1][-1]

    def minimumEffortPath_BS(self, heights: List[List[int]]) -> int:
        # BFS + Binary Search
        # O(mn logk), where k = 10**6

        low = 0
        high = 10 ** 6
        answer = math.inf

        while low <= high:
            mid = (low + high) // 2
            if self.is_reachable(heights, mid):
                answer = min(answer, mid)
                high = mid - 1

            else:
                low = mid + 1

        return answer

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra's
        # O(V logE), so O(mn log mn)

        heap = []

        m, n = len(heights), len(heights[0])

        distance = [[math.inf for _ in range(n)] for _ in range(m)]
        distance[0][0] = 0

        heapq.heappush(heap, (0, 0, 0))

        while heap:
            dist, i, j = heapq.heappop(heap)
            if dist > distance[i][j]:
                continue
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    next_dist = max(dist, abs(heights[i][j] - heights[x][y]))
                    if next_dist < distance[x][y]:
                        distance[x][y] = next_dist
                        heapq.heappush(heap, (next_dist, x, y))

        return distance[-1][-1]


