# 마법사 상어와 파이어스톰
# 골드 3
import copy
from collections import deque

n, q = map(int, input().split())
N = 2**n
mat = [list(map(int, input().split())) for _ in range(N)]
ls = list(map(int, input().split()))


def rotate(r, c, size, tmp):
    for i in range(0, size):
        for j in range(0, size):
            tmp[r + j][c + size-i-1] = mat[r + i][c + j]


def firestorm(l):
    size = 2 ** l
    result = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(0, N, size):
        for c in range(0, N, size):
            rotate(r, c, size, result)

    # deepcopy 이용 시 Pypy3로 통과
    # 별도의 melt 배열을 만들 시 Python3로 통과
    melt = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for neighbor in neighbors:
                if 0 <= neighbor[0] < N and 0 <= neighbor[1] < N:
                    if result[neighbor[0]][neighbor[1]] > 0:
                        cnt += 1
            if cnt < 3 and result[i][j] > 0:
                melt[i][j] -= 1

    for i in range(N):
        for j in range(N):
            if melt[i][j] != 0:
                result[i][j] += melt[i][j]

    return result


def bfs(r, c):
    q = deque()
    size = 0
    q.append((r, c))
    visited[r][c] = True
    while len(q) > 0:
        i, j = q.popleft()
        size += 1
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for neighbor in neighbors:
            if 0 <= neighbor[0] < N and 0 <= neighbor[1] < N:
                if not visited[neighbor[0]][neighbor[1]] and mat[neighbor[0]][neighbor[1]] > 0:
                    q.append(neighbor)
                    visited[neighbor[0]][neighbor[1]] = True
    return size


for l in ls:
    mat = firestorm(l)

sum_mat = 0
for i in range(N):
    sum_mat += sum(mat[i])
print(sum_mat)

visited = [[False for _ in range(N)] for _ in range(N)]

max_size = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))

print(max_size)
