# 새로운 게임 2
# 골드 2
import sys

n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]
mat_pieces = [[[] for _ in range(n)] for _ in range(n)]

pieces = [[] for _ in range(k)]
for i in range(k):
    r, c, d = map(int, input().split())
    pieces[i] = [r-1, c-1, d]


def reverse(num):
    if pieces[num][2] == 1:
        pieces[num][2] = 2
        return pieces[num][0], pieces[num][1]-1, pieces[num][2]

    if pieces[num][2] == 2:
        pieces[num][2] = 1
        return pieces[num][0], pieces[num][1]+1, pieces[num][2]

    if pieces[num][2] == 3:
        pieces[num][2] = 4
        return pieces[num][0]+1, pieces[num][1], pieces[num][2]

    if pieces[num][2] == 4:
        pieces[num][2] = 3
        return pieces[num][0]-1, pieces[num][1], pieces[num][2]



def move(num, d, r, c, isReverse = False):
    # r, c: 도착지
    # d: 새로운 방향 (blue)
    r_old = pieces[num][0]
    c_old = pieces[num][1]
    idx = mat_pieces[r_old][c_old].index(num)
    l = len(mat_pieces[r_old][c_old])

    for i in range(idx, l):
        piece = mat_pieces[r_old][c_old][i]
        pieces[piece][0] = r
        pieces[piece][1] = c
        if i == idx:
            pieces[piece][2] = d
            # blue의 경우, A번 말"만" 방향을 뒤집음
            # 그 외 색상에서는 방향이 바뀔 일이 없음
    # for piece in mat_pieces[r_old][c_old][idx:]:
    #     pieces[piece][0] = r
    #     pieces[piece][1] = c
    #     pieces[piece][2] = d

    if isReverse:
        mat_pieces[r][c] += list(reversed(mat_pieces[r_old][c_old][idx:]))
    else:
        mat_pieces[r][c] += mat_pieces[r_old][c_old][idx:]
    mat_pieces[r_old][c_old] = mat_pieces[r_old][c_old][:idx]

    if len(mat_pieces[r][c]) >= 4:
        return True  # 게임 종료
    return False


def move_try(num):
    r = pieces[num][0]
    c = pieces[num][1]
    d = pieces[num][2]

    if d == 1:
        c += 1
    elif d == 2:
        c -= 1
    elif d == 3:
        r -= 1
    else:
        r += 1

    if not (0 <= r < n and 0 <= c < n) or color[r][c] == 2:
        # blue
        r, c, d = reverse(num)
        if not (0 <= r < n and 0 <= c < n) or color[r][c] == 2:
            return False
        if color[r][c] == 1:
            return move(num, d, r, c, isReverse=True)
        return move(num, d, r, c)


    elif color[r][c] == 0:
        # white
        return move(num, d, r, c)

    else:
        # red
        return move(num, d, r, c, isReverse=True)



for num in range(k):
    r = pieces[num][0]
    c = pieces[num][1]
    mat_pieces[r][c].append(num)

for turn in range(1, 1001):
    for num in range(k):
        if move_try(num):
            print(turn)
            sys.exit()
print(-1)