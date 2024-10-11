# 가장 긴 증가하는 부분 수열 5
# 플래티넘 5

import bisect

n = int(input())
seq = list(map(int, input().split()))

answer = []
indices = [0 for _ in range(n)]

for i, num in enumerate(seq):
    idx = bisect.bisect_left(answer, num)
    if idx >= len(answer):
        answer.append(num)
    else:
        answer[idx] = num
    indices[i] = idx

print(len(answer))

LIS = []
target = len(answer) - 1
for i in range(n-1, -1, -1):
    if indices[i] == target:
        LIS.append(seq[i])
        target -= 1
    if target < 0:
        break
LIS.sort()

for x in LIS:
    print(x, end=' ')


