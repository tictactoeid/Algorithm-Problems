# 트리의 지름
# 골드 2

# 1967 트리의 지름과 똑같은 문제

# 시간 & 메모리 초과 발생하여, 백트래킹하지 않도록 (트리이므로) 변경, 입력 형식 변경
# 이외에는 똑같음

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

adj = [[] for _ in range(n)]


for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    node1 = line[0] - 1
    for i in range(1, len(line)-1, 2):
        node2 = line[i] - 1
        weight = line[i+1]
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
            # tree이므로 백트래킹할 필요 없음

v = [False for _ in range(n)]
v[0] = True
dfs(0, 0, v)
cost_max = 0

v = [False for _ in range(n)]
v[dst] = True
dfs(dst, 0, v)

print(cost_max)
