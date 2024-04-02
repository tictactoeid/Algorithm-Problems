# 최소비용 구하기
# 골드 5
import heapq
import math
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

bus = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    if bus[start][end] < 0:
        bus[start][end] = cost
    else:
        bus[start][end] = min(bus[start][end], cost)

start, end = map(int, sys.stdin.readline().split())
start -= 1
end -= 1

distance = [math.inf for _ in range(n)]
# distance[i]: start => i 로 가는 current min
distance[start] = 0
q = []
heapq.heappush(q, (0, start)) # (cost, node)
while q:
    cost, node = heapq.heappop(q) # 방문할 node
    if distance[node] < cost: # 갱신할 최소 거리가 없으므로, 그냥 무시
        continue

    for i in range(n):
        if bus[node][i] < 0: # 버스가 없는 경우
            continue
        # start -> node -> i
        new_cost = distance[node] + bus[node][i]
        if distance[i] > new_cost:
            distance[i] = new_cost
            heapq.heappush(q, (new_cost, i))

        # distance[node] + bus[node][i]: new cost
        # distance[i] : old cost

#print(distance)
print(distance[end])