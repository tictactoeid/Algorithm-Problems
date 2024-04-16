# 마법사 상어와 토네이도
# 골드 3

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

direction = 0
# 0 왼 1 아래 2 오른 3 위

length = 1
# 1칸 1칸 2칸 2칸 3칸 3칸 4칸 4칸 ... n-1칸 n-1칸 n-1칸
count = 0 # length만큼 이동한 횟수, 즉 방향을 바꾸어야 하는지?

tornado = (n//2, n//2)
sand_out = 0


def next_direction(d):
    return (d + 1) % 4


def next_move(direction, length, count, tornado):
    #print(direction, length, count, tornado)

    if direction == 0: # 왼쪽
        tornado = (tornado[0], tornado[1] - 1)
    elif direction == 1:
        tornado = (tornado[0] + 1, tornado[1])
    elif direction == 2:
        tornado = (tornado[0], tornado[1] + 1)
    else:
        tornado = (tornado[0] - 1, tornado[1])

    count += 1
    if count == length:
        direction = next_direction(direction)
    elif count == 2*length:
        direction = next_direction(direction)
        count = 0
        if length != n-1:
            length += 1


    return direction, length, count, tornado


def wind_sand(tornado, direction):
    global sand_out
    sand = mat[tornado[0]][tornado[1]]
    deltas = []
    alpha = (0, 0)
    if direction == 0:
        deltas = [(-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2), (-1, 1, 1),
                  (1, 1, 1), (-1, -1, 10), (1, -1, 10), (0, -2, 5)]
        alpha = (0, -1)
        # (-1, 0, 7): (r-1, c)로 7% 이동
    elif direction == 1:
        deltas = [(0, -1, 7), (0, 1, 7), (0, -2, 2), (0, 2, 2), (-1, -1, 1),
                  (-1, 1, 1), (1, -1, 10), (1, 1, 10), (2, 0, 5)]
        alpha = (1, 0)
    elif direction == 2:
        deltas = [(-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2), (-1, -1, 1),
                  (1, -1, 1), (-1, 1, 10), (1, 1, 10), (0, 2, 5)]
        alpha = (0, 1)
    else:
        deltas = [(0, -1, 7), (0, 1, 7), (0, -2, 2), (0, 2, 2), (1, -1, 1),
                  (1, 1, 1), (-1, -1, 10), (-1, 1, 10), (-2, 0, 5)]
        alpha = (-1, 0)

    for delta in deltas:
        r = tornado[0] + delta[0]
        c = tornado[1] + delta[1]
        percent = delta[2]
        amount = (sand * percent) // 100
        mat[tornado[0]][tornado[1]] -= amount
        if 0 <= r < n and 0 <= c < n:
            mat[r][c] += amount
        else:
            sand_out += amount
    # 나머지는 alpha로
    r = tornado[0] + alpha[0]
    c = tornado[1] + alpha[1]
    if 0 <= r < n and 0 <= c < n:
        mat[r][c] += mat[tornado[0]][tornado[1]]
    else:
        sand_out += mat[tornado[0]][tornado[1]]
    mat[tornado[0]][tornado[1]] = 0


while tornado != (0, 0):
    direction_next, length, count, tornado = next_move(direction, length, count, tornado)
    wind_sand(tornado, direction)
    direction = direction_next

wind_sand((0, 0), 0)
print(sand_out)