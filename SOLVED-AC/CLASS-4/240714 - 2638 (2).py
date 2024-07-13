# 치즈
# 골드 3

# 치즈마다 bfs를 돌리는 대신, 외부 공기 (0, 0)에서 bfs를 한 번만 시행
# Python3로 통과

from collections import deque

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    flag = False
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for ne in neighbors:
            if 0 <= ne[0] <= n-1 and 0 <= ne[1] <= m-1:
                if mat[ne[0]][ne[1]] >= 1:
                    mat[ne[0]][ne[1]] += 1 # 접촉
                    flag = True
                elif mat[ne[0]][ne[1]] == 0 and not visited[ne[0]][ne[1]]:
                    visited[ne[0]][ne[1]] = True
                    q.append(ne)

    return flag

time = 0
while True:
    next_mat = [[0 for _ in range(m)] for _ in range(n)]

    if not bfs():
        print(time)
        break

    for i in range(n):
        for j in range(m):
            if mat[i][j] >= 3: # 기본 1 + 2회 접촉 = 3
                mat[i][j] = 0
            elif mat[i][j] > 1:
                mat[i][j] = 1

    time += 1
