# Z
# 실버 1
import sys
sys.setrecursionlimit(10**9)

n, r, c = map(int, input().split())
mat = [[0 for _ in range(2**n)] for _ in range(2**n)]
order = 0


def z(x1, y1, x2, y2):
    # x1 <= x < x2
    # y1 <= y < y2

    global mat, order
    div = (x2 - x1) // 2
    if div == 1:
        mat[y1][x1] = order
        mat[y1][x1 + 1] = order + 1
        mat[y1 + 1][x1] = order + 2


        mat[y1+1][x1+1] = order + 3
        order += 4
        return
    else:
        # print(div)
        z(x1, y1, x1+div, y1+div)
        z(x1+div, y1, x2, y1+div)
        z(x1, y1+div, y1+div, y2)
        z(x1+div, y1+div, x2, y2)

z(0, 0, 2**n, 2**n)
print(mat)
print(mat[r][c])