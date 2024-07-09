# 연구소
# 골드 4
from itertools import combinations
from collections import deque
#for i in combinations([1, 2, 3, 4, 5], 3):

n, m = map(int, input().split())
lab = [[] for _ in range(n)]
lab_wall = [[] for _ in range(n)]

empty = []
virus = []
for i in range(n):
    lab[i] = list(map(int, input().split()))
    lab_wall[i] = (lab[i])[:]
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            empty.append((i, j))


q = deque()
visited = set()
region = len(empty) - 3
result = 0

def bfs():
    global region
    while len(q) > 0:
        node = q.popleft()
        visited.add(node)
        i = node[0]
        j = node[1]
        for x in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x[0] < n and 0 <= x[1] < m:
                if x not in visited and lab_wall[x[0]][x[1]] == 0:
                    q.append(x)
                    visited.add(x)
                    region -= 1

result = 0
for new_walls in combinations(empty, 3):
    for k in range(3):
        lab_wall[new_walls[k][0]][new_walls[k][1]] = 1

    visited = set()
    region = len(empty) - 3

    for i in virus:
        q = deque()
        q.append(i)
        bfs()

    result = max(result, region)

    for k in range(3):
        lab_wall[new_walls[k][0]][new_walls[k][1]] = 0

print(result)
