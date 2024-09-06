# 파티
# 골드 3

import math
import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(n)]
edges_rev = [[] for _ in range(n)]

for i in range(m):
    start, end, t = map(int, sys.stdin.readline().split())
    edges[start-1].append((end-1, t))
    edges_rev[end-1].append((start-1, t))

x -= 1
dist = [math.inf for _ in range(n)]
dist[x] = 0

q = []
heapq.heappush(q, (0, x))
while q:
    cost, node = heapq.heappop(q)
    if dist[node] < cost:
        continue # 갱신할 최소 거리가 없는 경우, 즉 이미 방문한 노드

    # start ~> node -> i
    for edge in edges[node]:
        i, w = edge

        new_cost = dist[node] + w
        if dist[i] > new_cost:
            dist[i] = new_cost
            heapq.heappush(q, (new_cost, i))

dist_rev = [math.inf for _ in range(n)]
dist_rev[x] = 0
q = []
heapq.heappush(q, (0, x))
while q:
    cost, node = heapq.heappop(q)
    if dist_rev[node] < cost:
        continue # 갱신할 최소 거리가 없는 경우, 즉 이미 방문한 노드

    # start ~> node -> i
    for edge in edges_rev[node]:
        i, w = edge

        new_cost = dist_rev[node] + w
        if dist_rev[i] > new_cost:
            dist_rev[i] = new_cost
            heapq.heappush(q, (new_cost, i))

for i in range(n):
    dist[i] += dist_rev[i]
print(max(dist))