# 욕심쟁이 판다
# 골드 3

# 1트: dfs를 n^2번, 당연히 시간 초과
# 2트: 방문한 적 없는 점에서 dfs를 수행, 이때 path를 기록하고 return 직전에 path 위 모든 점들에 대해 dfs_result 갱신
# dfs_result는 일종의 dp배열로, 해당 점에서 출발하여 갈 수 있는 칸의 최댓값
# 시간 초과

# 3트: path 기록 & return 직전에 갱신하는 방식 대신, 단순 dfs 수행
# 대신, dfs를 recursive하게 call하는 그 순간 dfs_result를 갱신

# current = dfs_result[i][j]
# new_path = dfs_modified(x, y) + 1
# dfs_result[i][j] = max(current, new_path)

import sys
sys.setrecursionlimit(10**6)

n = int(input())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2트
# dfs_result = [[1 for _ in range(n)] for _ in range(n)]
# def dfs_with_path(i, j, path):
#     neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
#     flag = False
#     for neighbor in neighbors:
#         x = neighbor[0]
#         y = neighbor[1]
#         if 0 <= x < n and 0 <= y < n:
#             if mat[x][y] > mat[i][j] and (x, y) not in path:
#                 flag = True
#                 dfs_with_path(x, y, path + [(x, y)])
#
#     if not flag:
#         #print(path)
#         for k in range(len(path)-1, -1, -1):
#             x = path[k][0]
#             y = path[k][1]
#             length = len(path) - k
#             dfs_result[x][y] = max(dfs_result[x][y], length)
#         #print(dfs_result)


# 3트
dfs_result = [[0 for _ in range(n)] for _ in range(n)]


def dfs_modified(i, j):
    if dfs_result[i][j]:
        return dfs_result[i][j]

    dfs_result[i][j] = 1  # 첫 방문

    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for neighbor in neighbors:
        x = neighbor[0]
        y = neighbor[1]
        if 0 <= x < n and 0 <= y < n:
            if mat[x][y] > mat[i][j]:
                current = dfs_result[i][j]
                new_path = dfs_modified(x, y) + 1
                dfs_result[i][j] = max(current, new_path)

    return dfs_result[i][j]


for i in range(n):
    for j in range(n):
        if not dfs_result[i][j]:
            dfs_modified(i, j)


print(max(max(dfs_result[i]) for i in range(len(dfs_result))))
