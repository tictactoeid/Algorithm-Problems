# 특정한 최단 경로
# 골드 4

import sys, heapq, math

n, e = map(int, sys.stdin.readline().split())
edges = [[math.inf for _ in range(n)] for _ in range(n)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    edges[a][b] = c # 간선은 0 or 1개 존재
    edges[b][a] = c

v1, v2 = map(int, sys.stdin.readline().split())
v1 -= 1
v2 -= 1

q = []
dist_1 = [math.inf for _ in range(n)]
dist_v1 = [math.inf for _ in range(n)]
dist_v2 = [math.inf for _ in range(n)]
dist_1[0] = 0
dist_v1[v1] = 0
dist_v2[v2] = 0

heapq.heappush(q, (0, 0)) # cost, node
while q:
    cost, node = heapq.heappop(q)
    if dist_1[node] < cost:
        continue

    for i in range(n): # start -> node -> i
        if edges[i][node] == math.inf:
            continue
        new_cost = edges[i][node] + dist_1[node]
        if dist_1[i] > new_cost:
            dist_1[i] = new_cost
            heapq.heappush(q, (new_cost, i))


q = []
heapq.heappush(q, (0, v1)) # cost, node
while q:
    cost, node = heapq.heappop(q)
    if dist_v1[node] < cost:
        continue

    for i in range(n): # start -> node -> i
        if edges[i][node] == math.inf:
            continue
        new_cost = edges[i][node] + dist_v1[node]
        if dist_v1[i] > new_cost:
            dist_v1[i] = new_cost
            heapq.heappush(q, (new_cost, i))


q = []
heapq.heappush(q, (0, v2)) # cost, node
while q:
    cost, node = heapq.heappop(q)
    if dist_v2[node] < cost:
        continue

    for i in range(n): # start -> node -> i
        if edges[i][node] == math.inf:
            continue
        new_cost = edges[i][node] + dist_v2[node]
        if dist_v2[i] > new_cost:
            dist_v2[i] = new_cost
            heapq.heappush(q, (new_cost, i))


# 1 -> v1 -> v2 -> n
cost_1 = dist_1[v1] + dist_v1[v2] + dist_v2[n-1]
cost_2 = dist_1[v2] + dist_v2[v1] + dist_v1[n-1]

result = min(cost_1, cost_2)
if result == math.inf:
    print(-1)
else:
    print(result)
