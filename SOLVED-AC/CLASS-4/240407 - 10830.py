# 행렬 제곱
# 골드 4
import sys
sys.setrecursionlimit(10**6)

n, b = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] %= 1000

def mult(mat1, mat2):
    new_mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_mat[i][j] += mat1[i][k] * mat2[k][j]
                new_mat[i][j] %= 1000
    return new_mat


def calc(mat, b):
    if b == 0 or b == 1:
        return mat
    elif b == 2:
        return mult(mat, mat)
    elif b % 2 == 0:
        half_mat = calc(mat, b//2)
        return mult(half_mat, half_mat)
    else:
        half_mat = calc(mat, b//2)
        return mult(mult(half_mat, half_mat), mat)


result = calc(mat, b)
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()