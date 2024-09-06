# 상범 빌딩
# 골드 5
from collections import deque

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break


    mat = [[] for _ in range(l)]
    for k in range(l):
        mat[k] = [input() for _ in range(r)]
        input()
    #print(mat)
    s = False

    for i in range(l):
        if s:
            break
        for j in range(r):
            if s:
                break
            for k in range(c):
                if mat[i][j][k] == 'S':
                    s = (i, j, k)
                    break

    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]

    q = deque()
    depth = 0
    q.append((s[0], s[1], s[2], depth))
    visited[s[0]][s[1]][s[2]] = True
    escaped = False
    while q:
        x, y, z, depth = q.popleft()
        neighbors = [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
        for node in neighbors:
            if 0 <= node[0] < l and 0 <= node[1] < r and 0 <= node[2] < c:
                if visited[node[0]][node[1]][node[2]]:
                    continue
                value = mat[node[0]][node[1]][node[2]]
                if value == 'E':
                    print("Escaped in {0} minute(s).".format(depth + 1))
                    escaped = True
                    break
                elif value == '#':
                    continue
                else:
                    q.append((node[0], node[1], node[2], depth + 1))
                    visited[node[0]][node[1]][node[2]] = True
        if escaped:
            break

    if not escaped:
        print("Trapped!")




