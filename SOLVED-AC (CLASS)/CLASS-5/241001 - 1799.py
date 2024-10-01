# 비숍
# 골드 1
import sys

n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
result = 0

# for i in range(n):
#     for j in range(n):
#         if mat[i][j]:
#             bishop_candidates.append((i, j))


def flatten(mat):
    flat = []
    for row in mat:
        flat += row

    return flat


def getter(arr, i, j):
    return arr[i*n + j]


def setter(arr, i, j, value):
    arr[i*n + j] = value
    return arr


def possible(arr, x, y):
    #for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    for di, dj in [(1, -1), (-1, 1)]:  # \ 방향은 diagonal loop에서 검사
        i = x
        j = y

        while 0 <= i < n and 0 <= j < n:
            if getter(arr, i, j) == 2:
                return False
            i += di
            j += dj

    return True


def backtracking(arr, count, start_diagonal=0):
    global result
    result = max(result, count)



    for diagonal in range(start_diagonal, 2*n - 1):
        remainder = 2 * n - 1 - diagonal
        if remainder + count <= result:
            return

        #print(f"diag {diagonal}")
        if diagonal < n:
            start = (0, n-1-diagonal)

        else:
            start = (diagonal-n+1, 0)

        # 해당 대각선에 비숍이 있는지 검사
        flag = False
        x, y = start
        while x < n and y < n:
            if getter(arr, x, y) == 2:
                flag = True
                break
            x += 1
            y += 1

        if flag:
            # 비숍이 있다면 해당 대각선은 고려할 필요가 없음
            continue

        # 백트래킹
        x, y = start
        while x < n and y < n:
            if getter(arr, x, y) == 0:
                x += 1
                y += 1
                continue
            # TODO: / 방향 검사?
            else:
                if possible(arr, x, y):
                    #print(x, y)
                    backtracking(setter(arr, x, y, 2), count+1, diagonal+1)
                    arr = setter(arr, x, y, 1)
                    #print(x, y, arr)
                    #arr = setter(arr, x, y, 1)

                    #
                    #
                    #
                    # new_mat = copy.deepcopy(mat)
                    # new_mat[x][y] = 2
                    # #print(mat)
                    # #print(new_mat)
                    # backtracking(new_mat, count+1, diagonal+1)
                    #     # mat[x][y] = 2
                    #     # backtracking(copy.deepcopy(mat), count+1)  # FIXME
                    #     # mat[x][y] = 1
                x += 1
                y += 1


backtracking(flatten(mat), 0, 0)
print(result)


