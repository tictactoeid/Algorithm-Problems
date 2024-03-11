# 경로 찾기
# 실버 1

import math

n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))
    #matrix[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] == 1 and matrix[k][j] == 1:  # path exists
                matrix[i][j] = 1


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
