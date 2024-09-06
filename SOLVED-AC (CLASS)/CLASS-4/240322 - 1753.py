# 최단경로
# 골드 5

import sys, math, heapq

n, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
k -= 1
edges = [[] for _ in range(n)]
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    edges[u].append([v, w])

    # edge 하나만 남기고 갱신하면 Pypy3로 통과, Python3에서 시간 초과
    # adjacency matrix 사용 시 메모리 초과, list 사용해야함
    # flag = False
    # for edge in edges[u]:
    #     if edge[0] == v:
    #         edge[1] = min(edge[1], w)
    #         flag = True
    #         break
    # if not flag:
    #     edges[u].append([v, w])
#print(edges[0])
# Dijkstra's

q = []
dist = [math.inf for _ in range(n)]
dist[k] = 0
heapq.heappush(q, (0, k))
while q:
    cost, node = heapq.heappop(q)
    if dist[node] < cost:
        continue
    for edge in edges[node]:
        next = edge[0]
        weight = edge[1]

        new_cost = dist[node] + weight
        if dist[next] > new_cost: # start ~> node -> next
            dist[next] = new_cost
            heapq.heappush(q, (new_cost, next))

for i in range(n):
    if dist[i] == math.inf:
        print('INF')
    else:
        print(dist[i])