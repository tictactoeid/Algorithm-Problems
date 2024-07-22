# 트리의 지름
# 골드 4

# 3트

# Pypy로 통과
# leaf node에서 dfs -> 잘못된 풀이

import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())

adj = [[] for _ in range(n)]
#parents = set()
#parent_start = 0
parents = [False for _ in range(n)]

for _ in range(n-1):
    node1, node2, weight = map(int, sys.stdin.readline().split())
    node1 -= 1
    node2 -= 1
    adj[node1].append((node2, weight))
    adj[node2].append((node1, weight))
    #parent_start = max(parent_start, node1)
    #parents.add(node1)
    parents[node1] = True


cost_max = 0


def dfs(node, cost, visited):
    global cost_max
    cost_max = max(cost, cost_max)

    for next, weight in adj[node]:
        if not visited[next]:
            visited[next] = True
            dfs(next, cost + weight, visited)
            visited[next] = False


for i in range(n):
    #if i not in parents:
    if not parents[i]:
        v = [False for _ in range(n)]
        v[i] = True
        dfs(i, 0, v)

print(cost_max)