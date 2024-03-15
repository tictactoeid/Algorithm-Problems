# 테트로미노
# 골드 4

import sys
n, m = map(int, input().split())

mat = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    mat[i] = line

tmp = 0
for i in range(n):
    for j in range(m):
        if i+3 < n:
            tmp = max(tmp, mat[i][j] + mat[i+1][j] + mat[i+2][j] + mat[i+3][j])
        if j+3 < m:
            tmp = max(tmp, sum(mat[i][j:j+4]))
        if i+1 < n and j+1 < m: # 2*2
            tmp = max(tmp, mat[i][j] + mat[i+1][j+1] + mat[i][j+1] + mat[i+1][j])

        if j+2 < m and i+1 < n:
            tmp = max(tmp,
                      mat[i][j] + mat[i][j+1] + mat[i+1][j+1] + mat[i+1][j+2],
                      mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j] + mat[i + 1][j + 1],
                      mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j + 1],
                      mat[i][j + 1] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 1][j + 2],
                      mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j],
                      mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j + 2],
                      mat[i][j] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 1][j + 2],
                      mat[i][j + 2] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 1][j + 2],
                      )
            #
            #
            # ㅁㅁ*
            # *ㅁㅁ
            #
            # *ㅁㅁ
            # ㅁㅁ*
            #
            # ㅁㅁㅁ
            # *ㅁ*
            #
            # *ㅁ*
            # ㅁㅁ
            #
            # ㅁㅁㅁ
            # ㅁ**
            #
            # ㅁㅁㅁ
            # **ㅁ
            #
            # ㅁ**
            # ㅁㅁㅁ
            #
            # **ㅁ
            # ㅁㅁㅁ
            # area = [mat[i][j], mat[i][j+1], mat[i+1][j], mat[i+1][j+1],
            #         mat[i+2][j], mat[i+2][j+1]]
            #
            # core = [mat[i + 1][j], mat[i + 1][j + 1]]
            # min1 = min(area)
            # area.remove(min1)
            # min2 = min(area)
            # if min1 not in core or min2 not in core:
            #     area.remove(min2)
            #     tmp = max(tmp, sum(area))
        if j+1 < m and i+2 < n:
            tmp = max(tmp,
                      mat[i][j] + mat[i+1][j] + mat[i+2][j] + mat[i+2][j+1],
                      mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 2][j] + mat[i + 2][j + 1],
                      mat[i][j] + mat[i][j + 1] + mat[i + 1][j] + mat[i + 2][j],
                      mat[i][j] + mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 2][j + 1],
                      mat[i][j] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 2][j + 1],
                      mat[i][j + 1] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 2][j],
                      mat[i][j + 1] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 2][j + 1],
                      mat[i][j] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 2][j],

            )
            # ㅁ*
            # ㅁ*
            # ㅁㅁ
            #
            # *ㅁ
            # *ㅁ
            # ㅁㅁ
            #
            # ㅁㅁ
            # ㅁ*
            # ㅁ*
            #
            # ㅁㅁ
            # *ㅁ
            # *ㅁ
            #
            # ㅁ*
            # ㅁㅁ
            # *ㅁ
            #
            # *ㅁ
            # ㅁㅁ
            # ㅁ*
            #
            # *ㅁ
            # ㅁㅁ
            # *ㅁ
            #
            # ㅁ*
            # ㅁㅁ
            # ㅁ*


print(tmp)








