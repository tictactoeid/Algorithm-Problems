# Cherry Pickup
# Hard

# greedy로는 해결 불가
# cherry를 줍고 돌아간다고 생각하지 말고,
# cherry를 2명의 사람이 동시에 줍는다고 생각하면
# state가 (r1, c1, r2, c2) 인 dp로 해결 가능 -> optimize: (r1, c1, r2), O(n^3)


class Solution:
    def dp(self, r1, c1, r2):
        c2 = r1 + c1 - r2

        if not (0 <= r1 < self.n and 0 <= c1 < self.n and 0 <= r2 < self.n and 0 <= c2 < self.n):
            return -math.inf

        # print(r1, c1, r2, c2)

        if self.grid[r1][c1] == -1 or self.grid[r2][c2] == -1:
            return -math.inf

        if r1 == self.n - 1 and c1 == self.n - 1:
            return self.grid[r1][c1]

        if (r1, c1, r2) in self.memo:
            return self.memo[(r1, c1, r2)]

        value = 0

        if self.grid[r1][c1] == 1:
            value += 1
        if self.grid[r2][c2] == 1 and (r1 != r2 or c1 != c2):
            value += 1

        value += max(
            self.dp(r1 + 1, c1, r2),
            self.dp(r1 + 1, c1, r2 + 1),
            self.dp(r1, c1 + 1, r2),
            self.dp(r1, c1 + 1, r2 + 1)
        )

        self.memo[(r1, c1, r2)] = value
        # print(r1, c1, r2, value)
        return value

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.memo = {}
        self.n = len(grid)
        self.grid = grid
        ret = max(0, self.dp(0, 0, 0))
        # print(self.memo)
        return ret
