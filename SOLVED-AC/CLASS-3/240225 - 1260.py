# DFS와 BFS
# 실버 2
from collections import deque

n, m, v = map(int, input().split())
dfs_visited = [False for _ in range(n)]
bfs_visited = [False for _ in range(n)]
bfs_queue = deque()
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    matrix[node1 - 1][node2 - 1] = 1
    matrix[node2 - 1][node1 - 1] = 1

def dfs(node):
    # if not dfs_visited[node]:
    dfs_visited[node] = True

    print(node+1, end=' ')

    for i in range(n):
        if matrix[node][i] and not dfs_visited[i]:
            dfs(i)

def bfs(node):
    bfs_queue.append(node)
    bfs_visited[node] = True
    print(node+1, end=' ')

    while bfs_queue:
        curr = bfs_queue.popleft()
        for i in range(n):
            if matrix[curr][i] and not bfs_visited[i]:
                bfs_queue.append(i)
                bfs_visited[i] = True
                print(i + 1, end=' ')


dfs(v - 1)
print()
bfs(v - 1)
