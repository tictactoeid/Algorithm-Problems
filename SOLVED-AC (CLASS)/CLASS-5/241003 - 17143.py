# 낚시왕
# 골드 1

r, c, m = map(int, input().split())

mat = [[[] for _ in range(c)] for _ in range(r)]

#sharks = [list(map(int, input().split())) for _ in range(m)]

for _ in range(m):
    i, j, d, s, z = map(int, input().split())
    mat[i-1][j-1] = [d, s, z]


def move(s, d, z, i, j, remain_dist=None):
    if remain_dist is None:
        remain_dist = s
    if d == 1:  # 위
        movable_dist = i
        if movable_dist >= remain_dist:
            return [s, d, z], i-remain_dist, j
        else:
            return move(s, 2, z, 0, j, remain_dist-movable_dist)
    elif d == 2:  # 아래
        movable_dist = r - 1 - i
        if movable_dist >= remain_dist:
            return [s, d, z], i+remain_dist, j
        else:
            return move(s, 1, z, r-1, j, remain_dist-movable_dist)
    elif d == 3:  # 오른쪽
        movable_dist = c - 1 - j
        if movable_dist >= remain_dist:
            return [s, d, z], i, j+remain_dist
        else:
            return move(s, 4, z, i, c-1, remain_dist-movable_dist)
    else:  # 왼쪽
        movable_dist = j
        if movable_dist >= remain_dist:
            return [s, d, z], i, j-remain_dist
        else:
            return move(s, 3, z, i, 0, remain_dist-movable_dist)


result = 0
for col in range(c):  # 낚시왕 이동
    # 상어 포획
    for row in range(r):
        if mat[row][col]:
            result += mat[row][col][2]
            mat[row][col] = []
            m -= 1
            break

    if col == c-1 or m == 0:
        break

    # 상어 이동
    new_mat = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not mat[i][j]:
                continue
            s, d, z = mat[i][j]
            shark, x, y = move(s, d, z, i, j, None)

            if new_mat[x][y]:  # 잡아먹음
                z2 = new_mat[x][y][2]
                if z2 > z:
                    continue
            new_mat[x][y] = shark

    #print(mat)
    #print(new_mat)
    mat = new_mat
print(result)