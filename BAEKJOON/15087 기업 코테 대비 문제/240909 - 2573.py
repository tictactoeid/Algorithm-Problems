# 빙산
# 골드 4
import sys
from collections import deque

# Pypy로 통과, Python3 시간초과
# 원래 Python으로는 시간이 부족한 문제인 듯

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]


def simulate(mat):
    new_mat = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            water_count = 0
            for neighbor in neighbors:
                x = neighbor[0]
                y = neighbor[1]
                if mat[x][y] == 0:
                    water_count += 1
            new_mat[i][j] = max(0, mat[i][j] - water_count)

    return new_mat


def is_one(mat):
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]

    start = None
    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                start = (i, j)

    if start is None:
        # 다 녹을 때까지 분리되지 않는 경우 0을 출력
        print(0)
        sys.exit()

    q.append(start)
    while q:
        i, j = q.popleft()
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            x = neighbor[0]
            y = neighbor[1]
            if 0 <= x < n and 0 <= y < m:
                if not visited[x][y] and mat[x][y]:
                    visited[x][y] = True
                    q.append((x, y))

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and mat[i][j]:
                return False

    return True


year = 0
while True:
    year += 1
    mat = simulate(mat)
    result = is_one(mat)
    if not result:
        print(year)
        break