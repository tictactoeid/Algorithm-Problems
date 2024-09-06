# 절댓값 힙
# 실버 1
import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q:
            a, b = heapq.heappop(q)
            print(b)
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x), x))