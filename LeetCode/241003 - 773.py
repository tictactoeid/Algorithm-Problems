# Sliding Puzzle
# Hard

import copy
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


class Solution:
    def __init__(self):
        self.target = "123450"
        self.answer = math.inf

    def get_zero_pos(self, board):
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return (i, j)

    def neighbors(self, board):
        x, y = self.get_zero_pos(board)
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        result = []
        for ne in neighbors:
            if 0 <= ne[0] < 2 and 0 <= ne[1] < 3:
                result.append(ne)
        return result

    def board_to_str(self, board):
        result = ""
        for i in range(2):
            for j in range(3):
                result += str(board[i][j])
        return result

    def swap(self, board, i1, j1, i2, j2):
        tmp = board[i1][j1]
        board[i1][j1] = board[i2][j2]
        board[i2][j2] = tmp
        return board

    def slidingPuzzle(self, board: list[list[int]]) -> int:
        board_str = self.board_to_str(board)
        if board_str == self.target:
            return 0

        visited = set()
        visited.add(board_str)

        q = deque()
        q.append((board, 0))

        while q:
            board, count = q.popleft()
            zero_x, zero_y = self.get_zero_pos(board)

            for x, y in self.neighbors(board):
                new_board = copy.deepcopy(board)
                self.swap(new_board, x, y, zero_x, zero_y)

                new_str = self.board_to_str(new_board)
                if new_str == self.target:
                    self.answer = min(self.answer, count + 1)
                if new_str in visited:
                    continue

                visited.add(self.board_to_str(new_board))
                q.append((new_board, count + 1))

        if self.answer == math.inf:
            return -1
        else:
            return self.answer
