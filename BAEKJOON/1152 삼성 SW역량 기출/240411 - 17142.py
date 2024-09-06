# 연구소 3
# 골드 3

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

empty_cnt = 0
virus_init = []
curr_min = -1

for i in range(n):
    for j in range(n):
        if mat[i][j] == 0:
            empty_cnt += 1
        elif mat[i][j] == 2:
            virus_init.append((i, j))


def bfs(virus_list, empty_cnt):
    global curr_min
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    time = 0
    for i in range(len(virus_list)):
        if virus_list[i]:
            q.append((virus_init[i][0], virus_init[i][1], time))

    while len(q) > 0:
        if empty_cnt == 0:
            break

        if curr_min != -1 and time > curr_min:
            return

        i, j, time = q.popleft()
        visited[i][j] = True
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for x, y in neighbors:
            if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                if mat[x][y] == 1:  # 벽
                    visited[x][y] = True
                    continue
                elif mat[x][y] == 0:
                    empty_cnt -= 1
                    if empty_cnt == 0:
                        time += 1
                        break
                    visited[x][y] = True
                    q.append((x, y, time + 1))
                else:  # 바이러스 (활성 or 비활성)
                    visited[x][y] = True
                    q.append((x, y, time + 1))

    if empty_cnt == 0:
        if curr_min == -1:
            curr_min = time
        else:
            curr_min = min(curr_min, time)


def backtrack(virus_list, start, cnt):
    if cnt == m:
        bfs(virus_list, empty_cnt)
    l = len(virus_init)
    for i in range(start, l):
        virus_list[i] = True
        backtrack(virus_list, i+1, cnt+1)
        virus_list[i] = False


virus_list = [False for _ in range(len(virus_init))]
backtrack(virus_list, 0, 0)
print(curr_min)
