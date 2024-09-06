# 구간 합 구하기 4
# 실버 3

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

p = list(map(int, sys.stdin.readline().rstrip().split()))

partial_sum = [0 for _ in range(len(p))]
partial_sum[0] = p[0]
for i in range(1, len(p)):
    partial_sum[i] = partial_sum[i-1] + p[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == 1:
        print(partial_sum[j-1])
    else:
        print(partial_sum[j-1] - partial_sum[i-2])

