# 치즈
# 골드 3

# dfs로 시간 초과
# bfs + Pypy로 통과

from collections import deque

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]


def air_bfs(r, c):
    if mat[r][c] == 1:
        return False

    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for ne in neighbors:
            if 0 <= ne[0] <= n-1 and 0 <= ne[1] <= m-1:
                if mat[ne[0]][ne[1]] == 0 and not visited[ne[0]][ne[1]]:
                    visited[ne[0]][ne[1]] = True
                    q.append(ne)
            else:
                return True

    return False


def melt(r, c):
    # print(r, c)
    cnt = 0
    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

    for ne in neighbors:
        #if air(ne[0], ne[1], [[False for _ in range(m)] for _ in range(n)]):
        if air_bfs(ne[0], ne[1]):
            cnt += 1
        if cnt >= 2:
            return True

    return False


time = 0
while True:
    flag = False
    next_mat = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                flag = True
                if not melt(i, j):
                    # print("melt")
                    next_mat[i][j] = 1

    if not flag:
        print(time)
        break

    time += 1
    mat = next_mat
