# 불!
# 골드 3
import math
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
mat = [sys.stdin.readline() for _ in range(r)]

# 1트: 지훈의 dist가 변할 때마다 mat에서 불 좌표를 실시간 갱신, 시간 초과
# 2트: 각 불에 대해 bfs, 불이 각 좌표에 도달하는 최소 거리를 기록하고 시작, Pypy 통과 / Python 시간 초과
# 3트: 불 전체를 bfs queue에 한 번에 넣고 1번만 bfs -> 이후 지훈 bfs, Python 통과


def fire_arrive_time(mat):
    fire_mat = [[math.inf for _ in range(c)] for _ in range(r)]
    fires = []
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '#':
                fire_mat[i][j] = '#'
            elif mat[i][j] == 'F':
                fire_mat[i][j] = 0
                fires.append((i, j))
            elif mat[i][j] == 'J':
                jihoon = (i, j)

    q = deque()
    dist = 0
    visited = [[False for _ in range(c)] for _ in range(r)]

    for (i, j) in fires:
        q.append((i, j, dist))
        visited[i][j] = True

    while q:
        i, j, dist = q.popleft()
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            x = neighbor[0]
            y = neighbor[1]
            if 0 <= x < r and 0 <= y < c:
                if not visited[x][y] and mat[x][y] != 'F' and mat[x][y] != '#':
                    fire_mat[x][y] = min(fire_mat[x][y], dist + 1)
                    visited[x][y] = True
                    q.append((x, y, dist + 1))

    return fire_mat, jihoon


def escape(mat):
    fire_mat, jihoon = fire_arrive_time(mat)

    q = deque()
    dist = 0
    visited = [[False for _ in range(c)] for _ in range(r)]
    q.append((jihoon[0], jihoon[1], dist))
    visited[jihoon[0]][jihoon[1]] = True

    while q:
        i, j, dist = q.popleft()

        if i == 0 or i == r-1 or j == 0 or j == c-1:
            return dist + 1

        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            x = neighbor[0]
            y = neighbor[1]
            if 0 <= x < r and 0 <= y < c:
                if not visited[x][y] and mat[x][y] != '#':
                    try:
                        if fire_mat[x][y] <= dist + 1:
                            continue
                    except TypeError:
                        pass
                    if x == 0 or x == r-1 or y == 0 or y == c-1:
                        return dist + 2  # 가장자리에서 한 칸 더 가야 하므로 +1이 아닌 +2

                    visited[x][y] = True
                    q.append((x, y, dist + 1))
    return "IMPOSSIBLE"

print(escape(mat))
