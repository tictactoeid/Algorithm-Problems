# 카드 짝 맞추기
# 레벨 3
# 2021 KAKAO BLIND RECRUITMENT

# 정확성 73.3 / 100
# 접근은 맞는데 결국 못 푼 문제
# 카드 방문 순서는 brute-force
# 최단 거리는 bfs 변형

import copy
from collections import deque
import math


def bfs(board, r1, c1, r2, c2):
    q = deque()
    q.append((0, r1, c1))
    visited = [[False for _ in range(4)] for _ in range(4)]
    visited[r1][c1] = True

    while q:
        dist, r, c = q.popleft()

        if r == r2 and c == c2:
            return dist

        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        # ctrl + arrow
        for x in range(r+1, 4):
            if (board[x][c] or x == 3) and (x, c) not in neighbors:
                neighbors.append((x, c))
                break

        for x in range(r-1, -1, -1):
            if (board[x][c] or x == 0) and (x, c) not in neighbors:
                neighbors.append((x, c))
                break

        for y in range(c+1, 4):
            if (board[r][y] or y == 3) and (r, y) not in neighbors:
                neighbors.append((r, y))
                break

        for y in range(c-1, -1, -1):
            if (board[r][y] or y == 0) and (r, y) not in neighbors:
                neighbors.append((r, y))
                break

        for x, y in neighbors:
            if 0 <= x < 4 and 0 <= y < 4:
                if not visited[x][y]:
                    visited[x][y] = True
                    q.append((dist+1, x, y))


value = math.inf


def remove_target_card(board, x, y):
    #x, y, dist1 = card
    target_card = board[x][y]
    for i in range(4):
        for j in range(4):
            if board[i][j] == target_card and (i, j) != (x, y):
                target = (i, j)
                dist2 = bfs(board, x, y, target[0], target[1])

                board[x][y] = 0
                board[target[0]][target[1]] = 0

                return board, target[0], target[1], dist2


def finished(board):
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                return False

    return True


def get_all_cards(board):
    result = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                result.append((i, j))
    return result


def solve(board, r, c, current_result=0):
    global value

    cards = get_all_cards(board)

    for card in cards:
        x, y = card
        dist1 = bfs(board, r, c, x, y)

        removed_board, next_r, next_c, dist2 = remove_target_card(copy.deepcopy(board), x, y)


        print(f"{r, c} -> {x, y} -> {next_r, next_c}, cnt {dist1+dist2+2}")
        print(f"{board} board")
        print(f"{removed_board} rm")
        if finished(removed_board):
            value = min(value, current_result + dist1 + dist2 + 2)
            print(current_result + dist1 + dist2 + 2)

        else:
            solve(removed_board, next_r, next_c, current_result + dist1 + dist2 + 2)


def solution(board, r, c):
    global value
    value = math.inf
    solve(board, r, c, 0)
    return value


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 	1, 	0))

#
# print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 	0 ,	1))
# print(solution([[0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 0, 3)) # 5
# print(solution( [[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0))  # 32
