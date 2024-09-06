# 쉬운 최단거리
# 실버 1

from collections import deque

n, m = map(int, input().split())

matrix = [[] for _ in range(n)]
start = ()
for i in range(n):
    matrix[i] = list(map(int, input().split()))
    if 2 in matrix[i]:
        start = (i, matrix[i].index(2))


def neighbors(node):
    neighbors = []
    if node[0] > 0:
        if matrix[node[0] - 1][node[1]] != 0:
            neighbors.append((node[0] - 1, node[1]))
    if node[0] < n-1:
        if matrix[node[0] + 1][node[1]] != 0:
            neighbors.append((node[0] + 1, node[1]))
    if node[1] > 0:
        if matrix[node[0]][node[1] - 1] != 0:
            neighbors.append((node[0], node[1] - 1))
    if node[1] < m-1:
        if matrix[node[0]][node[1] + 1] != 0:
            neighbors.append((node[0], node[1] + 1))
    return neighbors


depth = 0
q = deque()
visited = {}

q.append((start, depth))

while len(q) > 0:
    node, depth = q.popleft()
    visited[node] = depth
    for neighbor in neighbors(node):
        if neighbor not in visited.keys():
            q.append((neighbor, depth + 1))
            visited[neighbor] = depth + 1


for i in range(n):
    for j in range(m):
        if (i, j) not in visited.keys():
            if matrix[i][j] != 0:
                print(-1, end=' ')
            else:
                print(0, end=' ')
        else:
            print(visited[(i, j)], end=' ')
    print()




