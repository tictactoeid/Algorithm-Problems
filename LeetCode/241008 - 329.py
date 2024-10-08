# Longest Increasing Path in a Matrix
# Hard

from typing import *
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    path_length = []
    n = 0
    m = 0
    matrix = []

    def dfs_terminate(self, additional_path_len: int, path: List[Tuple[int]]):
        curr_path_len = len(path)
        # print(path)
        for i in range(curr_path_len - 1, -1, -1):
            x, y = path[i]
            self.path_length[x][y] = max(self.path_length[x][y], curr_path_len - i + additional_path_len)

    def dfs(self, r: int, c: int, path: List[Tuple[int]]):
        # visited 불필요할듯

        # self.path_length[r][c] = max(self.path_length[r][c], count)

        flag = False

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for x, y in neighbors:
            if 0 <= x < self.n and 0 <= y < self.m:
                if self.matrix[r][c] < self.matrix[x][y]:
                    flag = True
                    if self.path_length[x][y] == -1:
                        self.dfs(x, y, path + [(x, y)])
                    else:
                        self.dfs_terminate(self.path_length[x][y], path)

        if not flag:
            # terminate
            self.dfs_terminate(0, path)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.path_length = [[-1 for _ in range(self.m)] for _ in range(self.n)]
        self.matrix = matrix

        for i in range(self.n):
            for j in range(self.m):
                if self.path_length[i][j] == -1:
                    self.dfs(i, j, [(i, j)])
                else:
                    continue

        # self.dfs(2, 1, [(2, 1)])
        # print(self.path_length)
        return max(map(max, self.path_length))


