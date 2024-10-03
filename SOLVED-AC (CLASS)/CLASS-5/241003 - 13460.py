# 구슬 탈출 2
# 골드 1
import copy
import math

n, m = map(int, input().split())

mat = [[x for x in input()] for _ in range(n)]
result = math.inf


def up(mat):
    red_out = False
    blue_out = False
    for i in range(1, n-1):
        for j in range(1, m-1):
            if mat[i][j] == 'R' or mat[i][j] == 'B':
                dst = i
                for k in range(i-1, -1, -1):
                    if mat[k][j] == '.':
                        dst = k
                        continue
                    elif mat[k][j] == 'O':
                        if mat[i][j] == 'R':
                            red_out = True
                        elif mat[i][j] == 'B':
                            blue_out = True
                        mat[i][j] = '.'
                        break
                    else:
                        if dst != i:
                            mat[dst][j] = mat[i][j]
                            mat[i][j] = '.'
                        break
    #print_mat(mat)
    return mat, red_out, blue_out


def down(mat):
    red_out = False
    blue_out = False
    for i in range(n-2, 0, -1):
        for j in range(1, m-1):
            if mat[i][j] == 'R' or mat[i][j] == 'B':
                dst = i
                for k in range(i+1, n):
                    if mat[k][j] == '.':
                        dst = k
                        continue
                    elif mat[k][j] == 'O':
                        if mat[i][j] == 'R':
                            red_out = True
                        elif mat[i][j] == 'B':
                            blue_out = True
                        mat[i][j] = '.'
                        break
                    else:
                        if dst != i:
                            mat[dst][j] = mat[i][j]
                            mat[i][j] = '.'
                        break
    #print_mat(mat)
    return mat, red_out, blue_out




def left(mat):
    red_out = False
    blue_out = False
    for j in range(1, m-1):
        for i in range(1, n-1):
            if mat[i][j] == 'R' or mat[i][j] == 'B':
                dst = j
                for k in range(j-1, -1, -1):
                    if mat[i][k] == '.':
                        dst = k
                        continue
                    elif mat[i][k] == 'O':
                        if mat[i][j] == 'R':
                            red_out = True
                        elif mat[i][j] == 'B':
                            blue_out = True
                        mat[i][j] = '.'
                        break
                    else:
                        if dst != j:
                            mat[i][dst] = mat[i][j]
                            mat[i][j] = '.'
                        break
    #print_mat(mat)
    return mat, red_out, blue_out


def right(mat):
    red_out = False
    blue_out = False
    for j in range(m-2, 0, -1):
        for i in range(1, n-1):
            if mat[i][j] == 'R' or mat[i][j] == 'B':
                dst = j
                for k in range(j+1, m):
                    if mat[i][k] == '.':
                        dst = k
                        continue
                    elif mat[i][k] == 'O':
                        if mat[i][j] == 'R':
                            red_out = True
                        elif mat[i][j] == 'B':
                            blue_out = True
                        mat[i][j] = '.'
                        break
                    else:
                        if dst != j:
                            mat[i][dst] = mat[i][j]
                            mat[i][j] = '.'
                        break
    #print_mat(mat)
    return mat, red_out, blue_out


def print_mat(mat):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end='')
        print()


def try_move(mat, last_move, count):
    global result
    if count == 10:
        return
    elif count >= result:
        return

    # 0 UP
    # 1 DOWN
    # 2 LEFT
    # 3 RIGHT
    if last_move != 0:
        up_mat, red_out, blue_out = up(copy.deepcopy(mat))
        if red_out or blue_out:
            if red_out and not blue_out:
                result = min(result, count+1)
        elif mat != up_mat:
            try_move(up_mat, 0, count+1)

    if last_move != 1:
        down_mat, red_out, blue_out = down(copy.deepcopy(mat))
        if red_out or blue_out:
            if red_out and not blue_out:
                result = min(result, count+1)
        elif mat != down_mat:
            try_move(down_mat, 1, count+1)

    if last_move != 2:
        left_mat, red_out, blue_out = left(copy.deepcopy(mat))
        if red_out or blue_out:
            if red_out and not blue_out:
                result = min(result, count+1)
        elif mat != left_mat:
            try_move(left_mat, 2, count+1)

    if last_move != 3:
        right_mat, red_out, blue_out = right(copy.deepcopy(mat))
        if red_out or blue_out:
            if red_out and not blue_out:
                result = min(result, count+1)
        elif mat != right_mat:
            try_move(right_mat, 3, count+1)

try_move(mat, -1, 0)
if result == math.inf:
    print(-1)
else:
    print(result)
