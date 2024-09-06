# 어른 상어
# 골드 2
import copy
import sys

n, m, k = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# [상어 번호, 시간]

mat_next = [[0 for _ in range(n)] for _ in range(n)]
smell_next = [[[0, 0] for _ in range(n)] for _ in range(n)]

directions = [0] + list(map(int, sys.stdin.readline().split()))
directions_next = [0 for _ in range(m+1)]

priors = [0, 0, 0, 0] + [list(map(int, sys.stdin.readline().split())) for _ in range(4*m)]

shark_cnt = m

def next_coordinates(prior):
    result = []
    for dir_next in prior:
        # try: no smell
        di = 0
        dj = 0
        if dir_next == 1:
            di -= 1
        elif dir_next == 2:
            di += 1
        elif dir_next == 3:
            dj -= 1
        else:
            dj += 1
        x = i + di
        y = j + dj
        if 0 <= x < n and 0 <= y < n:
            result.append((x, y, dir_next))
    return result


def move(i, j):
    global shark_cnt
    shark = mat[i][j]
    direction_curr = directions[shark]
    prior = priors[shark * 4 + direction_curr - 1]
    next_coord = next_coordinates(prior)

    for x, y, dir_next in next_coord:
        # no smell
        if smell[x][y][1] == 0:
            if mat_next[x][y] != 0:
                shark_cnt -= 1
                mat_next[x][y] = min(mat_next[x][y], shark)
                smell_next[x][y] = [min(mat_next[x][y], shark), k]
                directions_next[shark] = dir_next
            else:
                mat_next[x][y] = shark
                smell_next[x][y] = [shark, k]
                directions_next[shark] = dir_next
            return

    for x, y, dir_next in next_coord:
        # my smell
        if smell[x][y][0] == shark:
            if mat_next[x][y] != 0:
                shark_cnt -= 1
                mat_next[x][y] = min(mat_next[x][y], shark)
                smell_next[x][y] = [min(mat_next[x][y], shark), k]
                directions_next[shark] = dir_next
            else:
                mat_next[x][y] = shark
                smell_next[x][y] = [shark, k]
                directions_next[shark] = dir_next
            return

    smell_next[i][j] = [shark, k]
    # 이동하지 않는 상어도 냄새를 뿌림.....?
    return

# 0초에 냄새를 뿌리고 시작
for i in range(n):
    for j in range(n):
        if mat[i][j] != 0:
            smell[i][j] = [mat[i][j], k]

for t in range(1, 1001):


    mat_next = [[0 for _ in range(n)] for _ in range(n)]
    smell_next = [[[0, 0] for _ in range(n)] for _ in range(n)]
    directions_next = [0 for _ in range(m + 1)]

    # 기존 냄새 옅어짐
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] <= 1:
                continue
            smell_next[i][j] = [smell[i][j][0], smell[i][j][1] - 1]
            # move()에서 이동하면서 냄새까지 뿌릴 것
            # 이때 기존 냄새를 덮어씌워야 하므로, 기존 냄새 -1은 미리 해놔야 함
            # 대신 move()에서 판단 기준은 smell (old)로 해야 함

    # 이동 및 냄새 뿌리기
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                continue
            move(i, j)

    if shark_cnt == 1:
        print(t)
        break

    mat = copy.deepcopy(mat_next)
    smell = copy.deepcopy(smell_next)
    directions = copy.deepcopy(directions_next)


if shark_cnt != 1: # 1000초가 지났는데도
    print(-1)
