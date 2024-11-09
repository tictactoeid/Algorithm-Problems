# 01 Matrix
# Medium

class Solution:
    def updateMatrix_bfs(self, mat: List[List[int]]) -> List[List[int]]:
        # Approach 1: BFS
        # BFS를 한 점에서 시작하는 대신
        # 모든 0인 점을 queue에 넣고 시작함
        # O(mn)
        m, n = len(mat), len(mat[0])

        ans = [[-1 for _ in range(n)] for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ans[i][j] = 0

        while q:
            i, j, dist = q.popleft()

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if ans[x][y] != -1:  # visited
                        continue
                    ans[x][y] = dist + 1
                    q.append((x, y, dist + 1))

        return ans

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Approach 2: DP
        # 단순하게 순회하게 되면 아래 / 오른쪽 방향을 cover하지 못하므로
        # 두 번 순회함
        # O(mn)
        m, n = len(mat), len(mat[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    left = dp[i][j - 1] + 1 if j > 0 else math.inf
                    up = dp[i - 1][j] + 1 if i > 0 else math.inf
                    dp[i][j] = min(left, up)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                right = dp[i][j + 1] + 1 if j < n - 1 else math.inf
                down = dp[i + 1][j] + 1 if i < m - 1 else math.inf
                dp[i][j] = min(dp[i][j], right, down)

        return dp
