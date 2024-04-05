# 최소 힙
# 실버 2
import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)