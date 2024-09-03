# 새로운 게임
# 골드 2
import sys

n, k = map(int, input().split())
mat = [[] for _ in range(n)]
piece = [[] for _ in range(k)]

stacks = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    mat[i] = list(map(int, input().split()))

for i in range(k):
    tmp = list(map(int, input().split()))
    i_curr = tmp[0] - 1
    j_curr = tmp[1] - 1
    stacks[i_curr][j_curr] = [i]
    piece[i] = [i_curr, j_curr, tmp[2]]


def move_to_white(x, i_next, j_next):
    i_curr = piece[x][0]
    j_curr = piece[x][1]
    stack = stacks[i_curr][j_curr]

    # 같이 이동
    for p in stack:
        piece[p][0] = i_next
        piece[p][1] = j_next

    # 같이 이동
    stacks[i_next][j_next] += stack
    stacks[i_curr][j_curr] = []

    if len(stacks[i_next][j_next]) >= 4:
        return True  # 종료
    return False


def move_to_red(x, i_next, j_next):
    i_curr = piece[x][0]
    j_curr = piece[x][1]
    stack = stacks[i_curr][j_curr]

    # 같이 이동
    for p in stack:
        piece[p][0] = i_next
        piece[p][1] = j_next

    # 같이 이동
    stacks[i_next][j_next] += reversed(stack)
    stacks[i_curr][j_curr] = []

    if len(stacks[i_next][j_next]) >= 4:
        return True  # 종료
    return False


def move_to_blue(x):
    direction = piece[x][2]
    if direction == 1:
        piece[x][2] = 2
    elif direction == 2:
        piece[x][2] = 1
    elif direction == 3:
        piece[x][2] = 4
    elif direction == 4:
        piece[x][2] = 3

    i_next, j_next = get_next_position(x)

    if not (0<=i_next<n and 0<=j_next<n):
        return False

    if mat[i_next][j_next] == 2:
        return False
    elif mat[i_next][j_next] == 0:
        return move_to_white(x, i_next, j_next)
    else:
        return move_to_red(x, i_next, j_next)


def get_next_position(x):
    i_curr = piece[x][0]
    j_curr = piece[x][1]
    direction = piece[x][2]

    if direction == 1:
        i_next = i_curr
        j_next = j_curr + 1
    elif direction == 2:
        i_next = i_curr
        j_next = j_curr - 1
    elif direction == 3:
        i_next = i_curr - 1
        j_next = j_curr
    elif direction == 4:
        i_next = i_curr + 1
        j_next = j_curr

    return i_next, j_next


def move_try(x):  # x번 말이 이동
    # if not 아래
    # pass
    i_curr = piece[x][0]
    j_curr = piece[x][1]

    stack = stacks[i_curr][j_curr]

    if stack[0] != x:
        return False

    i_next, j_next = get_next_position(x)

    if 0 <= i_next < n and 0 <= j_next < n:
        if mat[i_next][j_next] == 2:
            return move_to_blue(x)
        elif mat[i_next][j_next] == 0:
            return move_to_white(x, i_next, j_next)
        else:
            return move_to_red(x, i_next, j_next)
    else:
        return move_to_blue(x)


for t in range(1, 1000):
    for x in range(k):
        end = move_try(x)
        if end:
            print(t)
            sys.exit()

print(-1)
