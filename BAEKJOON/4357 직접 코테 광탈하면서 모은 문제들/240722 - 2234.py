# 성곽
# 골드 3

from collections import deque

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(m)]
room_mat = [[0 for _ in range(n)] for _ in range(m)] # 해당 칸이 몇 번 방 소속인지


def left_wall(i, j): # True if exists
    num = mat[i][j]
    return (num >> 0) % 2


def up_wall(i, j):
    num = mat[i][j]
    return (num >> 1) % 2


def right_wall(i, j):
    num = mat[i][j]
    return (num >> 2) % 2


def down_wall(i, j):
    num = mat[i][j]
    return (num >> 3) % 2


rooms = [0] # i번째 방의 넓이, 0번 원소는 invalid

# bfs를 해서, 방의 개수와 각 방의 넓이를 구한다
# rooms와 room_mat를 채운다
# room_mat를 순회한다. 이웃한 두 칸이 벽으로 막혀있는지 판단하고, 막혀 있다면 두 칸이 소속한 벽의 넓이를 더한다.
# 그렇게 더한 넓이들 중 최댓값을 구한다: O(n^2)


def bfs(start_i, start_j, room_no):
    if room_mat[start_i][start_j]:
        return

    area = 0
    q = deque()

    q.append((start_i, start_j))

    while q:
        i, j = q.popleft()
        if room_mat[i][j]: # visited
            continue

        area += 1
        room_mat[i][j] = room_no

        if i > 0 and not up_wall(i, j):
            q.append((i-1, j))

        if i < m-1 and not down_wall(i, j):
            q.append((i+1, j))

        if j > 0 and not left_wall(i, j):
            q.append((i, j-1))

        if j < n-1 and not right_wall(i, j):
            q.append((i, j+1))
    return area


room_no = 0
for i in range(m):
    for j in range(n):
        if not room_mat[i][j]:
            room_no += 1
            area = bfs(i, j, room_no)
            #rooms[room_no] = area
            rooms.append(area)
# 성곽
# 골드 3

from collections import deque

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(m)]
room_mat = [[0 for _ in range(n)] for _ in range(m)] # 해당 칸이 몇 번 방 소속인지


def left_wall(i, j): # True if exists
    num = mat[i][j]
    return (num >> 0) % 2


def up_wall(i, j):
    num = mat[i][j]
    return (num >> 1) % 2


def right_wall(i, j):
    num = mat[i][j]
    return (num >> 2) % 2


def down_wall(i, j):
    num = mat[i][j]
    return (num >> 3) % 2


rooms = [0] # i번째 방의 넓이, 0번 원소는 invalid

# bfs를 해서, 방의 개수와 각 방의 넓이를 구한다
# rooms와 room_mat를 채운다
# room_mat를 순회한다. 이웃한 두 칸이 벽으로 막혀있는지 판단하고, 막혀 있다면 두 칸이 소속한 벽의 넓이를 더한다.
# 그렇게 더한 넓이들 중 최댓값을 구한다: O(n^2)


def bfs(start_i, start_j, room_no):
    if room_mat[start_i][start_j]:
        return

    area = 0
    q = deque()

    q.append((start_i, start_j))

    while q:
        i, j = q.popleft()
        if room_mat[i][j]: # visited
            continue

        area += 1
        room_mat[i][j] = room_no

        if i > 0 and not up_wall(i, j):
            q.append((i-1, j))

        if i < m-1 and not down_wall(i, j):
            q.append((i+1, j))

        if j > 0 and not left_wall(i, j):
            q.append((i, j-1))

        if j < n-1 and not right_wall(i, j):
            q.append((i, j+1))
    return area


room_no = 0
for i in range(m):
    for j in range(n):
        if not room_mat[i][j]:
            room_no += 1
            area = bfs(i, j, room_no)
            #rooms[room_no] = area
            rooms.append(area)

print(len(rooms) - 1)
print(max(rooms))

result = 0
for i in range(m):
    for j in range(n):
        if i < m-1 and down_wall(i, j) and room_mat[i][j] != room_mat[i+1][j]:
            result = max(result, rooms[room_mat[i][j]] + rooms[room_mat[i+1][j]])

        if j < n-1 and right_wall(i, j) and room_mat[i][j] != room_mat[i][j+1]:
            result = max(result, rooms[room_mat[i][j]] + rooms[room_mat[i][j+1]])

print(result)

print(len(rooms) - 1)
print(max(rooms))

result = 0
for i in range(m):
    for j in range(n):
        if i < m-1 and down_wall(i, j) and room_mat[i][j] != room_mat[i+1][j]:
            result = max(result, rooms[room_mat[i][j]] + rooms[room_mat[i+1][j]])

        if j < n-1 and right_wall(i, j) and room_mat[i][j] != room_mat[i][j+1]:
            result = max(result, rooms[room_mat[i][j]] + rooms[room_mat[i][j+1]])

print(result)
