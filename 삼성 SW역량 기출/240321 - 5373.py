# 큐빙
# 플래티넘 5
import copy

# 위, 아래, 앞, 오른쪽, 뒤, 왼쪽
U = 0
D = 1
F = 2
R = 3
B = 4
L = 5
cube = [[[]], [[]], [[]], [[]], [[]], [[]]]


def reset():
    global cube
    cube[U] = [['w' for _ in range(3)] for _ in range(3)]
    cube[D] = [['y' for _ in range(3)] for _ in range(3)]
    cube[F] = [['r' for _ in range(3)] for _ in range(3)]
    cube[R] = [['b' for _ in range(3)] for _ in range(3)]
    cube[B] = [['o' for _ in range(3)] for _ in range(3)]
    cube[L] = [['g' for _ in range(3)] for _ in range(3)]


# 윗면: 위에서 봤을 때 왼쪽 위가 0, 0. 즉, 왼면 - 뒷면에 붙어있는
# 아랫면: 앞면, 왼면 (0, 0)
# 그 외: 윗면에 붙어있는 쪽이 0. (왼쪽 위가 0, 0)


def rotate(method):
    global cube
    #rotated = copy.deepcopy(cube)

    if method[0] == 'F':
        info = [[[U, 2, 0], [U, 2, 1], [U, 2, 2]],
                [[R, 0, 0], [R, 1, 0], [R, 2, 0]],
                [[D, 0, 2], [D, 0, 1], [D, 0, 0]],
                [[L, 2, 2], [L, 1, 2], [L, 0, 2]]]

        # TODO: F도 회전시켜야함

        # 회전할 12개의 큐브를 위 3개 - 오른 - 아래 - 왼 순으로 시계방향으로 기록, 기준면을 앞으로 둔다고 생각
        # 윗면의 (2, 0), (2, 1), (2, 2)
        # 오른쪽의 (0, 0), (1, 0), (2, 0)
        # 아래쪽의 (0, 2), (0, 1), (0, 0)
        # 왼쪽의 (2, 2), (1, 2), (0, 2)
    elif method[0] == 'B':
        info = [[[U, 0, 2], [U, 0, 1], [U, 0, 0]],
                [[L, 0, 0], [L, 1, 0], [L, 2, 0]],
                [[D, 2, 0], [D, 2, 1], [D, 2, 2]],
                [[R, 2, 2], [R, 1, 2], [R, 0, 2]]]
    elif method[0] == 'L':
        info = [[[U, 0, 0], [U, 1, 0], [U, 2, 0]],
                [[F, 0, 0], [F, 1, 0], [F, 2, 0]],
                [[D, 0, 0], [D, 1, 0], [D, 2, 0]],
                [[B, 2, 2], [B, 1, 2], [B, 0, 2]]]
    elif method[0] == 'R':
        info = [[[U, 2, 2], [U, 1, 2], [U, 0, 2]],
                [[B, 0, 0], [B, 1, 0], [B, 2, 0]],
                [[D, 2, 2], [D, 1, 2], [D, 0, 2]],
                [[F, 2, 2], [F, 1, 2], [F, 0, 2]]]
    elif method[0] == 'U':
        info = [[[B, 0, 2], [B, 0, 1], [B, 0, 0]],
                [[R, 0, 2], [R, 0, 1], [R, 0, 0]],
                [[F, 0, 2], [F, 0, 1], [F, 0, 0]],
                [[L, 0, 2], [L, 0, 1], [L, 0, 0]]]

    else:  # method[0] == 'D':
        info = [[[F, 2, 0], [F, 2, 1], [F, 2, 2]],
                [[R, 2, 0], [R, 2, 1], [R, 2, 2]],
                [[B, 2, 0], [B, 2, 1], [B, 2, 2]],
                [[L, 2, 0], [L, 2, 1], [L, 2, 2]]]

    tmp = [[0 for _ in range(4)] for _ in range(3)]
    for j in range(4):
        if method[1] == '+':
            # 3 -> 0
            # 0 -> 1
            # 1 -> 2
            # 2 -> 3
            #k = (j + 1) % 4
            k = (4 + j - 1) % 4
        else:
            # 3 <- 0
            # 0 <- 1
            # 1 <- 2
            # 2 <- 3
            #k = (4 + j - 1) % 4
            k = (j + 1) % 4
        #print(k,'->',j)
        for i in range(3):
            tmp[i][j] = cube[info[k][i][0]][info[k][i][1]][info[k][i][2]]
    for j in range(4):
        for i in range(3):
            cube[info[j][i][0]][info[j][i][1]][info[j][i][2]] = tmp[i][j]
    # 00 01 -> 02 12
    # 02 12 -> 22 21
    # 22 21 -> 20 10
    # 20 10 -> 00 01
    face = eval(method[0])
    if method[1] == '+':
        tmp[0][2] = cube[face][0][0]
        tmp[1][2] = cube[face][0][1]
        tmp[2][2] = cube[face][0][2]
        tmp[2][1] = cube[face][1][2]

        tmp[2][0] = cube[face][2][2]
        tmp[1][0] = cube[face][2][1]
        tmp[0][0] = cube[face][2][0]
        tmp[0][1] = cube[face][1][0]
    else:
        tmp[0][0] = cube[face][0][2]
        tmp[0][1] = cube[face][1][2]
        tmp[0][2] = cube[face][2][2]
        tmp[1][2] = cube[face][2][1]

        tmp[2][2] = cube[face][2][0]
        tmp[2][1] = cube[face][1][0]
        tmp[2][0] = cube[face][0][0]
        tmp[1][0] = cube[face][0][1]
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            cube[face][i][j] = tmp[i][j]



t = int(input())
out = ""
for _ in range(t):
    reset()
    n = int(input())
    methods = list(input().split())
    for method in methods:
        rotate(method)
        # for i in range(6):
        #     for j in range(3):
        #         print(cube[i][j])
        #     print()
        # print("-------")
    for i in range(3):
        for j in range(3):
            out += cube[U][i][j]
        out += "\n"

print(out)