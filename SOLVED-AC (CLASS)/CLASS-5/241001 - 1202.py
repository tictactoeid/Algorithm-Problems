# 보석 도둑
# 골드 2

import sys
import heapq

n, k = map(int, input().split())

gems = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [(int(sys.stdin.readline())) for _ in range(k)]
bags.sort()

#heapq.heapify(gems, key=lambda x: ())
gems.sort(key=lambda x: (x[0], -x[1]))

heap = []

idx = 0
result = 0
for bag in bags:
    while idx < n and gems[idx][0] <= bag:
        heapq.heappush(heap, -gems[idx][1])  # max heap
        idx += 1

    if heap:
        result -= heapq.heappop(heap)

print(result)

