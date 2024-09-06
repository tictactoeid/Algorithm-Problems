# Gaaaaaaaaaarden
# 골드 1
import copy
from itertools import combinations
from collections import deque

# Pypy로 통과
# deepcopy() 대신, color만의 matrix를 따로 만들고
# 각 조합마다 해당 matrix만 변경하면 Python으로도 통과할 듯

n, m, g, r = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

# 배양액 뿌리기
candidates = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            candidates.append((i, j))


def bfs(mat, comb):
    q = deque()
    count = 0

    visited = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    for x, y in comb:
        q.append((x, y, 0, mat[x][y]))
        if mat[x][y] == 'G':
            visited[x][y][0] = 0
        else:
            visited[x][y][1] = 0
    while q:
        x, y, time, color = q.popleft()
        if mat[x][y] == 'F':
            continue
        if mat[x][y] == 1 or mat[x][y] == 2:
            print(f"{x} {y} {mat[x][y]} to {color}")
            mat[x][y] = color
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for i, j in neighbors:
            if 0 <= i < n and 0 <= j < m:
                if color == 'G':
                    # TODO
                    if mat[i][j] == 1 or mat[i][j] == 2:
                        if visited[i][j][0] < 0:
                            visited[i][j][0] = time+1
                            mat[i][j] = color
                            q.append((i, j, time+1, color))
                    elif mat[i][j] == 'R':
                        if visited[i][j][1] == time+1:
                            mat[i][j] = 'F'
                            count += 1
                elif color == 'R':
                    if mat[i][j] == 1 or mat[i][j] == 2:
                        if visited[i][j][1] < 0:
                            visited[i][j][1] = time+1
                            mat[i][j] = color
                            q.append((i, j, time+1, color))
                    elif mat[i][j] == 'G':
                        if visited[i][j][0] == time+1:
                            mat[i][j] = 'F'
                            count += 1
    return count


flowers = 0
for comb in combinations(candidates, g+r):
    for current in combinations(comb, g):
        mat = copy.deepcopy(matrix)
        for x, y in comb:
            if (x, y) in current:
                mat[x][y] = 'G'
            else:
                mat[x][y] = 'R'
        flowers = max(bfs(mat, comb), flowers)

print(flowers)
