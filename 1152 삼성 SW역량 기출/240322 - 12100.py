# 2048 (Easy)
# 골드 2
import copy
import itertools

n = int(input())
board = [[] for _ in range(n)]
init_board = [[] for _ in range(n)]
init_max = 0
local_max = 0
result = 0

LEFT = "LEFT"
RIGHT = "RIGHT"
UP = "UP"
DOWN = "DOWN"

for i in range(n):
    board[i] = list(map(int, input().split()))
    init_board[i] = board[i][:]
    init_max = max(init_max, max(init_board[i]))

local_max = init_max


def move(direction):
    global local_max
    modified = [[False for _ in range(n)] for _ in range(n)]

    if direction == UP:
        for i in range(1, n): # 어디부터
            for k in range(n):
                for j in range(i, 0, -1): # 어디까지
                    if board[j][k] == 0:
                        break
                    if board[j][k] == board[j-1][k] and not modified[j-1][k] and not modified[j][k]:
                        board[j-1][k] *= 2
                        board[j][k] = 0
                        modified[j-1][k] = True
                        local_max = max(local_max, board[j-1][k])
                    elif board[j-1][k] == 0:
                        board[j-1][k] = board[j][k]
                        board[j][k] = 0
                        modified[j-1][k] = modified[j][k]
                        modified[j][k] = False
                    else:
                        break
    elif direction == DOWN:
        for i in range(n-1, -1, -1):
            for k in range(n):
                for j in range(i, n-1):
                    if board[j][k] == 0:
                        break
                    if board[j][k] == board[j+1][k] and not modified[j+1][k] and not modified[j][k]:
                        board[j+1][k] *= 2
                        board[j][k] = 0
                        modified[j+1][k] = True
                        local_max = max(local_max, board[j + 1][k])
                    elif board[j+1][k] == 0:
                        board[j+1][k] = board[j][k]
                        board[j][k] = 0
                        modified[j + 1][k] = modified[j][k]
                        modified[j][k] = False
                    else:
                        break
    elif direction == LEFT:
        for i in range(1, n):
            for k in range(n):
                for j in range(i, 0, -1): # 어디까지
                    if board[k][j] == 0:
                        break
                    if board[k][j] == board[k][j-1] and not modified[k][j-1] and not modified[k][j]:
                        board[k][j-1] *= 2
                        board[k][j] = 0
                        modified[k][j-1] = True
                        local_max = max(local_max, board[k][j-1])
                    elif board[k][j-1] == 0:
                        board[k][j-1] = board[k][j]
                        board[k][j] = 0
                        modified[k][j-1] = modified[k][j]
                        modified[k][j] = False
                    else:
                        break
    elif direction == RIGHT:
        for i in range(n-1, -1, -1):
            for k in range(n):
                for j in range(i, n-1):
                    if board[k][j] == 0:
                        break
                    if board[k][j] == board[k][j+1] and not modified[k][j+1] and not modified[k][j]:
                        board[k][j+1] *= 2
                        board[k][j] = 0
                        modified[k][j+1] = True
                        local_max = max(local_max, board[k][j+1])
                    elif board[k][j+1] == 0:
                        board[k][j+1] = board[k][j]
                        board[k][j] = 0
                        modified[k][j + 1] = modified[k][j]
                        modified[k][j] = False
                    else:
                        break
#
# print(board)
# move(RIGHT)
# print(board)
# move(UP)
# print(board)
# move(RIGHT)
# print(board)
# move(DOWN)
# print(board)
# move(UP)
# print(board)
# print(local_max)


for i in itertools.product([UP, DOWN, RIGHT, LEFT], repeat=5):
    #print(i)
    board = copy.deepcopy(init_board)
    local_max = init_max
    for j in range(5):
        move(i[j])
        # print(i[j])
    result = max(result, local_max)
    # print(board)
    # print(local_max)

print(result)