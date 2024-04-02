# 트리의 부모 찾기
# 실버 2
import sys
sys.setrecursionlimit(10**6)
n = int(input())

edges = [[] for _ in range(n)]
visited = [False for _ in range(n)]
parent = [0 for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def dfs(node):
    visited[node] = True
    for i in edges[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)

dfs(0)
#print(visited)
for i in range(1, n):
    print(parent[i]+1)

