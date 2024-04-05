# 아기 상어
# 골드 3

from collections import deque
n = int(input())
shark = (0, 0)
size = 2
count = 0

mat = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mat[i][j] == 9:
            shark = (i, j)
            mat[i][j] = 0
            break


def search(shark, size):
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    depth = 0
    q.append((shark, depth))
    visited[shark[0]][shark[1]] = True
    candidates = []
    dist = -1

    while len(q) > 0:
        shark, depth = q.popleft()
        x = shark[0]
        y = shark[1]
        visited[x][y] = True

        if 0 < dist < depth:
            break

        status = mat[x][y]
        if 0 < status < size: # can eat
            candidates.append(shark)
            if dist < 0:
                dist = depth

        neighbors = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
        for next in neighbors:
            if 0 <= next[0] < n and 0 <= next[1] < n and not visited[next[0]][next[1]]:
                if mat[next[0]][next[1]] > size:
                    continue
                else:
                    visited[next[0]][next[1]] = True
                    # visited 여기서 갱신해야 큐 중복 걸러져서 시간/메모리 초과 예방
                    q.append((next, depth + 1))
                # elif status == size or status == 0:
                #     q.append((next, depth + 1))
                # elif 0 < status < size:
                #     candidates.append((next, depth + 1))
                #     dist = depth + 1

    if candidates:
        candidates.sort(key=lambda x: (x[0], x[1]))
        # print(candidates, dist, depth)
        return candidates[0], dist
    return None, None


time = 0
prev_time = 0
while True:
    prev_time += time
    shark, time = search(shark, size)
    if shark is None:
        print(prev_time)
        break

    count += 1
    # print(shark[0], shark[1], size)
    mat[shark[0]][shark[1]] = 0
    if count == size:
        count = 0
        size += 1






