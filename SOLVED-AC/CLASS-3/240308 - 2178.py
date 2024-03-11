# 미로 탐색
# 실버 1

from collections import deque

q = deque()
visited = set()

n, m = map(int, input().split())

matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(m):
        matrix[i][j] = int(line[j])


def neighbors(node):
    neighbors = []

    if node[0] > 0 and matrix[node[0]-1][node[1]] == 1:
        neighbors.append((node[0]-1, node[1]))
    if node[0] < n-1 and matrix[node[0]+1][node[1]] == 1:
        neighbors.append((node[0]+1, node[1]))

    if node[1] > 0 and matrix[node[0]][node[1]-1] == 1:
        neighbors.append((node[0], node[1]-1))
    if node[1] < m-1 and matrix[node[0]][node[1]+1] == 1:
        neighbors.append((node[0], node[1]+1))

    return neighbors


depth = 1
node = (0, 0)
visited.add(node)
q.append((node, depth))

while len(q) > 0:
    node, depth = q.popleft()
    if node == (n-1, m-1):
        print(depth)
        break

    for neighbor in neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            q.append((neighbor, depth + 1))


