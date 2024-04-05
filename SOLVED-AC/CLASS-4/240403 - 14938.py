# 서강그라운드
# 골드 4

import sys
import math

n, m, r = map(int, sys.stdin.readline().split())

items = list(map(int, sys.stdin.readline().split()))
mat = [[math.inf for _ in range(n)] for _ in range(n)]
result = [0 for _ in range(n)]
for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    mat[a][b] = l
    mat[b][a] = l

for i in range(n):
    mat[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # i ~> k -> j
            new_cost = mat[i][k] + mat[k][j]
            if mat[i][j] > new_cost:
                mat[i][j] = new_cost
#print(mat)
for i in range(n):
    for j in range(n):
        if mat[i][j] <= m:
            result[i] += items[j]

print(max(result))