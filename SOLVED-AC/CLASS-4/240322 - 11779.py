# 최소비용 구하기 2
# 골드 3

import sys, heapq, math

n = int(input())
m = int(input())
edges = [[math.inf for _ in range(n)] for _ in range(n)]

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    edges[u][v] = min(w, edges[u][v])

start, stop = map(int, sys.stdin.readline().split())
start -= 1
stop -= 1

q = []
dist = [(math.inf, None) for _ in range(n)]
dist[start] = (0, None)
heapq.heappush(q, (0, start))
while q:
    cost, node = heapq.heappop(q)
    # start ~> node -> i
    if cost > dist[node][0]: # 갱신할 것이 없음.
        continue
    for i in range(n):
        if edges[node][i] == math.inf:
            continue

        next_cost = dist[node][0] + edges[node][i]

        if next_cost < dist[i][0]:
            dist[i] = (next_cost, node)
            heapq.heappush(q, (next_cost, i))


cost = dist[stop][0]
before = dist[stop][1]
count = 1
result = str(stop+1)
while before is not None:
    result = str(before+1) + " " + str(result)
    count += 1
    before = dist[before][1]
print(cost)
print(count)
print(result)