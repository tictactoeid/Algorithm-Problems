# 대표 선수
# 골드 2

import sys
import heapq
from collections import deque

n, m = map(int, sys.stdin.readline().split())
students = [deque(sorted(list(map(int, sys.stdin.readline().split())))) for _ in range(n)]

heap = []

min_value = int(10e9)
max_value = 0

for i in range(len(students)):
    v = students[i].popleft()
    max_value = max(max_value, v)
    min_value = min(min_value, v)
    heapq.heappush(heap, [v, i])

summation = max_value - min_value

while heap:
    prev_min_value, pos = heapq.heappop(heap)
    if not students[pos]:
        break

    new_value = students[pos].popleft()
    heapq.heappush(heap, [new_value, pos])

    if max_value < new_value:
        max_value = new_value
    min_value = heap[0][0]
    summation = min(summation, max_value - min_value)


print(summation)
