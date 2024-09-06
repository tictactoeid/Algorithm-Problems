# 흙길 보수하기
# 골드 5

import math

n, l = map(int, input().split())

waters = [list(map(int, input().split())) for _ in range(n)]
waters.sort()

last_tree = 0
count = 0

for water in waters:
    start = water[0]
    end = water[1]

    if last_tree >= end:  # 이미 덮여있음
        continue
    elif last_tree < start:  # 덮여있지 않음
        last_tree = start + l
        count += 1
    # 반쯤 덮여있음
    remainders = (end - last_tree)
    if remainders <= 0:
        continue
    count += math.ceil(remainders / l)
    last_tree += math.ceil(remainders / l) * l

print(count)
