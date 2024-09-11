# 용액
# 골드 5

import math, bisect

n = int(input())
liquids = list(map(int, input().split()))

current = [math.inf, None, None]  # 특성값 합, 특성값 1, 특성값 2

for i in range(n):
    liquid = liquids[i]
    target = 0 - liquid
    target_idx = bisect.bisect_left(liquids, target)

    for j in range(target_idx-1, target_idx+2):
        if j == i:
            continue
        else:
            if 0 <= j < n:
                tmp = liquids[j]
                value = liquid + tmp
                if abs(value) < abs(current[0]):
                    current = [value, liquid, tmp]

print(current[1], current[2])

