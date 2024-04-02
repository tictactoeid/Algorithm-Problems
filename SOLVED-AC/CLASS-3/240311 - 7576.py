# 토마토
# 골드 5

from collections import deque
import sys

m, n = map(int, input().split())
tomatoes = [[] for _ in range(n)]
count = 0
for i in range(n):
    tomatoes[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    count += tomatoes[i].count(0)



# 0 토마토의 개수를 저장하고 1로부터 bfs .. ?

def neighbors(node):
    result = []
    if node[0] > 0 and tomatoes[node[0]-1][node[1]] != -1:
        result.append((node[0]-1, node[1]))
    if node[0] < n-1 and tomatoes[node[0]+1][node[1]] != -1:
        result.append((node[0]+1, node[1]))
    if node[1] > 0 and tomatoes[node[0]][node[1]-1] != -1:
        result.append((node[0], node[1]-1))
    if node[1] < m-1 and tomatoes[node[0]][node[1]+1] != -1:
        result.append((node[0], node[1]+1))
    return result


def bfs(node):
    visited = set()
    q = deque()
    depth = 0
    q.append((node, depth))
    while len(q) > 0:
        current, depth = q.popleft()
        if tomatoes[current[0]][current[1]] == 1:
            return depth

        for neighbor in neighbors(current):
            if neighbor not in visited:

                if tomatoes[neighbor[0]][neighbor[1]] == 1:
                    return depth + 1

                visited.add(neighbor)
                q.append((neighbor, depth + 1))

    return -1

start = (-1, -1)
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            start = (i, j)
            break

def output():
    result = 0
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 0:
                value = bfs((i, j))
                if value == -1:
                    return -1
                result = max(result, value)

    return result


print(output())


