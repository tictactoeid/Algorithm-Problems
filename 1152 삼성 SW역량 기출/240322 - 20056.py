# 마법사 상어와 파이어볼
# 골드 4
import sys
from collections import deque

N, M, K = map(int, input().split())

mat = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []

for i in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    #mat[r][c].append([m, s, d])
    fireballs.append([r-1, c-1, m, s, d])

for _ in range(K):
    # Phase 1: 이동
    mat = [[[] for _ in range(N)] for _ in range(N)]
    for fireball in fireballs:
        r, c, m, s, d = fireball
        dr = 0
        dc = 0
        if d == 0 or d == 1 or d == 7:
            dr = -1
        if d == 3 or d == 4 or d == 5:
            dr = +1
        if d == 1 or d == 2 or d == 3:
            dc = +1
        if d == 7 or d == 6 or d == 5:
            dc = -1
        dr *= s
        dc *= s
        r = (r + dr) % N
        c = (c + dc) % N
        mat[r][c].append([m, s, d])

    # Phase 2: 합체
    fireballs = []

    for i in range(N):
        for j in range(N):
            if len(mat[i][j]) > 1:
                isOdd = False
                isEven = False
                cnt = len(mat[i][j])
                mass = 0
                vel = 0
                for fireball in mat[i][j]:
                    m, s, d = fireball
                    mass += m
                    vel += s
                    if d % 2 == 0:
                        isEven = True
                    else:
                        isOdd = True
                mass = mass // 5
                if mass == 0:
                    continue
                vel = vel // cnt
                if isOdd and isEven:
                    # 1, 3 ,5, 7
                    #mat[i][j] =
                    for k in range(1, 8, 2):
                        fireballs.append([i, j, mass, vel, k])
                else:
                    for k in range(0, 8, 2):
                        fireballs.append([i, j, mass, vel, k])

            elif len(mat[i][j]) == 1: # 합체 X
                m, s, d = mat[i][j][0]
                fireballs.append([i, j, m, s, d])
            else:
                continue

print(sum(map(lambda x: x[2], fireballs)))