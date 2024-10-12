# Game of Life
# Medium

# In-place

from itertools import product
from enum import Enum


class State(Enum):
    DEAD = 0
    LIVE = 1
    DIE_NEXT = 2  # LIVE currently; DEAD nextly
    LIVE_NEXT = 3  # DEAD currently; LIVE nextly


class Solution:
    def __init__(self):
        self.board = [[]]
        self.m = 0
        self.n = 0

        self.deltas = list(product([-1, 0, 1], repeat=2))
        self.deltas.remove((0, 0))

    def isAlive(self, i: int, j: int) -> bool:
        value = self.board[i][j]
        if value == State.LIVE.value or value == State.DIE_NEXT.value:
            return True
        else:
            return False

    def countLivingNeighbors(self, i: int, j: int) -> int:
        living_neighbors = 0
        for di, dj in self.deltas:
            x, y = i + di, j + dj
            if 0 <= x < self.m and 0 <= y < self.n:
                if self.isAlive(x, y):
                    living_neighbors += 1

        return living_neighbors

    def nextPhase(self) -> None:
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == State.LIVE_NEXT.value:
                    self.board[i][j] = State.LIVE.value
                elif self.board[i][j] == State.DIE_NEXT.value:
                    self.board[i][j] = State.DEAD.value

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        self.board = board

        for i in range(self.m):
            for j in range(self.n):
                living_neighbors = self.countLivingNeighbors(i, j)
                # print(living_neighbors)
                if self.isAlive(i, j):
                    if living_neighbors < 2:
                        # under-population
                        self.board[i][j] = State.DIE_NEXT.value
                    elif living_neighbors < 4:
                        if self.board[i][j] == State.DIE_NEXT.value:  # 근데 그럴 일이 있나?
                            self.board[i][j] = State.LIVE.value
                    else:
                        # over-population
                        self.board[i][j] = State.DIE_NEXT.value
                else:
                    if living_neighbors == 3:
                        # reproduction
                        self.board[i][j] = State.LIVE_NEXT.value
        # print(self.board)
        self.nextPhase()





