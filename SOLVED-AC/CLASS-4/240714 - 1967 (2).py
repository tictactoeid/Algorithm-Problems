# 트리의 지름
# 골드 4

# 4트

import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())

adj = [[] for _ in range(n)]

for _ in range(n-1):
    node1, node2, weight = map(int, sys.stdin.readline().split())
    node1 -= 1
    node2 -= 1
    adj[node1].append((node2, weight))
    adj[node2].append((node1, weight))


cost_max = 0
dst = 0

def dfs(node, cost, visited):
    global cost_max, dst
    if cost > cost_max:
        dst = node
        cost_max = cost

    for next, weight in adj[node]:
        if not visited[next]:
            visited[next] = True
            dfs(next, cost + weight, visited)
            visited[next] = False


v = [False for _ in range(n)]
v[0] = True
dfs(0, 0, v)

cost_max = 0
v = [False for _ in range(n)]
v[dst] = True
dfs(dst, 0, v)

print(cost_max)

# 임의의 node에 대하여, 해당 node로부터 가장 먼 점을 찾는다.
# 그 점으로부터, 가장 먼 점을 찾는다.
# 찾은 두 점이 지름의 양 끝이다.
