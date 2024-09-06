# 청소년 상어
# 골드 2
import copy

num = [[0 for _ in range(4)] for _ in range(4)]
direction = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            num[i][j//2] = line[j]
        else:
            direction[i][j//2] = line[j] - 1


def swap(i1, j1, sharkx, sharky, cnt, num, direction):
    if cnt == 8:
        return
    i2 = i1
    j2 = j1
    d = (direction[i1][j1] + cnt) % 8
    if d == 0:
        i2 -= 1
    elif d == 1:
        i2 -= 1
        j2 -= 1
    elif d == 2:
        j2 -= 1
    elif d == 3:
        i2 += 1
        j2 -= 1
    elif d == 4:
        i2 += 1
    elif d == 5:
        i2 += 1
        j2 += 1
    elif d == 6:
        j2 += 1
    else:
        i2 -= 1
        j2 += 1

    if i2 == sharkx and j2 == sharky:
        return swap(i1, j1, sharkx, sharky, cnt+1, num, direction)

    if not (0 <= i2 <= 3 and 0 <= j2 <= 3):
        return swap(i1, j1, sharkx, sharky, cnt+1, num, direction)

    if num[i2][j2] == 0:
        # 빈 공간
        num[i2][j2] = num[i1][j1]
        direction[i2][j2] = d
        num[i1][j1] = 0
        direction[i1][j1] = 0
        return

    else:
        # 다른 물고기
        num[i1][j1], num[i2][j2] = num[i2][j2], num[i1][j1]
        direction[i1][j1], direction[i2][j2] = direction[i2][j2], d
        return


def move_fish(num, direction, sharkx, sharky):
    for fish in range(1, 17):
        x = -1
        y = -1
        for i in range(4):
            for j in range(4):
                if num[i][j] == fish:
                    x = i
                    y = j
                    break
        if x < 0:
            continue
        else:
            swap(x, y, sharkx, sharky, 0, num, direction)


def backtracking(x, y, d, score, num, direction):
    global max_score
    # 잡아먹고
    score += num[x][y]
    #print(score, x, y, d)

    num[x][y] = 0
    d = direction[x][y]
    direction[x][y] = 0
    max_score = max(max_score, score)

    # 물고기 이동하고
    move_fish(num, direction, x, y)
    #print(num)
    dx = 0
    dy = 0

    if d == 0:
        dx -= 1
    elif d == 1:
        dx -= 1
        dy -= 1
    elif d == 2:
        dy -= 1
    elif d == 3:
        dx += 1
        dy -= 1
    elif d == 4:
        dx += 1
    elif d == 5:
        dx += 1
        dy += 1
    elif d == 6:
        dy += 1
    else:
        dx -= 1
        dy += 1

    # 상어 이동하고
    x += dx
    y += dy
    while 0 <= x <= 3 and 0 <= y <= 3:
        if num[x][y] == 0:
            x += dx
            y += dy
            continue
        else:

            # 백트래킹으로 반복하고
            backtracking(x, y, d, score, copy.deepcopy(num), copy.deepcopy(direction))
            x += dx
            y += dy


max_score = 0
backtracking(0, 0, 7, 0, copy.deepcopy(num), copy.deepcopy(direction))
print(max_score)