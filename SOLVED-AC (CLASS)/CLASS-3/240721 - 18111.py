# 마인크래프트
# 실버 2

import math
import sys

n, m, b = map(int, sys.stdin.readline().split())
#mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height_cnts = [0 for _ in range(257)]
for i in range(n):
    hs = list(map(int, sys.stdin.readline().split()))
    for h in hs:
        height_cnts[h] += 1


def make(target_level, inven_blks):
    time = 0
    # for i in range(n):
    #     for j in range(m):
    #         if mat[i][j] > target_level:
    #             inven_blks += (mat[i][j] - target_level)
    #             time += 2 * (mat[i][j] - target_level)
    #         elif mat[i][j] < target_level:
    #             inven_blks -= (target_level - mat[i][j])
    #             time += 1 * (target_level - mat[i][j])

    for i in range(257):
        if i > target_level:
            inven_blks += (i - target_level) * height_cnts[i]
            time += 2 * (i - target_level) * height_cnts[i]
        elif i < target_level:
            inven_blks -= (target_level - i) * height_cnts[i]
            time += 1 * (target_level - i) * height_cnts[i]

    if inven_blks < 0:
        #print(inven_blks)
        return -1
    return time


#while True:


min_time = math.inf
min_time_lev = 0

# brute_force
for level in range(257):
    result = make(level, b)
    #print(result, level)
    if result >= 0:
        if result < min_time:
            min_time_lev = level
            min_time = result
        elif result == min_time:
            min_time_lev = max(min_time_lev, level)
    # else:
    #     break


print(min_time, min_time_lev)

# binary_search

