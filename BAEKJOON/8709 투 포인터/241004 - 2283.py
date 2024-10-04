# 구간 자르기
# 골드 2

import sys

n, k = map(int, input().split())

lines = [tuple(map(int, input().split())) for _ in range(n)]

prefix_sum = [0 for _ in range(1000002)]

for line in lines:
    start, end = line
    prefix_sum[start+1] += 1
    prefix_sum[end+1] -= 1

for x in range(1, 1000002):
    prefix_sum[x] += prefix_sum[x-1]

# for x in range(1, 1000002):
#     prefix_sum[x] += prefix_sum[x-1]



start = 0
end = 0
value = sum(prefix_sum[start:end+1])  # 0

while start <= end and end < 1000001:

    if value == k:
        print(start, end)
        sys.exit()
    elif value > k:
        start += 1
        value -= prefix_sum[start]

    else:
        end += 1
        value += prefix_sum[end]




print(0, 0)
