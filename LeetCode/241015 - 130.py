# Surrounded Regions
# Medium

from collections import deque


class Solution:
    def bfs(self, board: List[List[str]], i: int, j: int) -> None:
        if board[i][j] != "O":
            return

        visited = set()

        q = deque()
        q.append((i, j))
        visited.add((i, j))
        while q:
            i, j = q.popleft()
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for r, c in neighbors:
                if 0 <= r < self.m and 0 <= c < self.n:
                    if board[r][c] == "O" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                else:
                    return

        for i, j in visited:
            board[i][j] = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        self.m = m
        self.n = n

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    self.bfs(board, i, j)

