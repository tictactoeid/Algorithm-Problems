# 감시 피하기
# 골드 5

import sys

n = int(input())

mat = [list(input().split()) for _ in range(n)]


def valid(matrix):
    students = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'S':
                students.append((i, j))

    for x, y in students:
        for i in range(x+1, n):
            if mat[i][y] == 'O':
                break
            if mat[i][y] == 'T':
                return False
        for i in range(x-1, -1, -1):
            if mat[i][y] == 'O':
                break
            if mat[i][y] == 'T':
                return False
        for j in range(y+1, n):
            if mat[x][j] == 'O':
                break
            if mat[x][j] == 'T':
                return False
        for j in range(y-1, -1, -1):
            if mat[x][j] == 'O':
                break
            if mat[x][j] == 'T':
                return False

    print("YES")
    sys.exit()


def coord(i):
    # 0 ~ n*n-1 -> (0, 0) ~ (n-1, n-1)
    return (i // n, i % n)


for i in range(n*n):
    x1, y1 = coord(i)
    if mat[x1][y1] == 'X':
        mat[x1][y1] = 'O'
        for j in range(i+1, n*n):
            x2, y2 = coord(j)
            if mat[x2][y2] == 'X':
                mat[x2][y2] = 'O'
                for k in range(j+1, n*n):
                    x3, y3 = coord(k)
                    if mat[x3][y3] == 'X':
                        mat[x3][y3] = 'O'
                        valid(mat)
                        mat[x3][y3] = 'X'
                mat[x2][y2] = 'X'
        mat[x1][y1] = 'X'

print("NO")
