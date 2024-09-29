# 부분합
# 골드 4

import math

n, s = map(int, input().split())

sequence = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n+1)]

prefix_sum[0] = 0

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + sequence[i]

result = math.inf

start = 0
end = 1

while start <= end <= n:
    summation = prefix_sum[end] - prefix_sum[start]
    if summation >= s:
        result = min(result, end-start)
        start += 1
    else:
        end += 1


if result != math.inf:
    print(result)
else:
    print(0)
