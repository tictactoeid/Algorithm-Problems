# 미세먼지 안녕!
# 골드 4
import copy
import sys
r, c, t = map(int, input().split())
mat = [[] for _ in range(r)]
total = 0
cleaner_up = None
cleaner_down = None

for i in range(r):
    mat[i] = list(map(int, sys.stdin.readline().split()))
    total += sum(mat[i])
    if cleaner_up is None:
        for j in range(c):
            if mat[i][j] == -1:
                cleaner_up = (i, j)
                cleaner_down = (i+1, j)

total += 2

for time in range(t):
    # 확산
    next_mat = copy.deepcopy(mat)
    for i in range(r):
        for j in range(c):
            if mat[i][j] > 0:
                amount = mat[i][j] // 5
                #print(amount)
                #print(i, j)
                #print(mat[i][j])
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x <= r-1 and 0 <= y <= c-1 and (x, y) != cleaner_up and (x, y) != cleaner_down:
                        next_mat[i][j] -= amount
                        next_mat[x][y] += amount



    # 바람 - 위 (반시계)
    total -= next_mat[cleaner_up[0]-1][cleaner_up[1]]
    total -= next_mat[cleaner_down[0]+1][cleaner_down[1]]
    if time == t-1:
        break
        # 어차피 total만 알면 되기 때문에, 마지막 회차에는 갱신할 필요가 없음

    cleaned_mat = copy.deepcopy(next_mat)
    for i in range(cleaner_up[0]-1, 0, -1):
        # (1, cleaner_up[1]) ~ (cleaner_up[0]-1, cleaner_up[1])
        # 한 칸씩 아래로 이동!
        cleaned_mat[i][cleaner_up[1]] = next_mat[i-1][cleaner_up[1]]
    for j in range(cleaner_up[1], c-1):
        # (0, cleaner_up[1]) ~ (0, c-2)
        # 한 칸씩 왼쪽으로 이동
        cleaned_mat[0][j] = next_mat[0][j+1]
    for i in range(0, cleaner_up[0]):
        # (0, c-1) ~ (cleaner_up[0]-1, c-1)
        # 위로 이동
        cleaned_mat[i][c-1] = next_mat[i+1][c-1]

    cleaned_mat[cleaner_up[0]][cleaner_up[1]+1] = 0
    for j in range(cleaner_up[1]+2, c):
        # 오른쪽
        cleaned_mat[cleaner_up[0]][j] = next_mat[cleaner_up[0]][j-1]

    # 바람 - 아래 (시계)
    cleaned_mat[cleaner_down[0]][cleaner_down[1]+1] = 0
    for j in range(cleaner_down[1]+2, c):
        # 오른쪽
        cleaned_mat[cleaner_down[0]][j] = next_mat[cleaner_down[0]][j-1]
    for i in range(cleaner_down[0]+1, r):
        # (0, c-1) ~ (cleaner_up[0]-1, c-1)
        # 아래
        cleaned_mat[i][c-1] = next_mat[i-1][c-1]
    for j in range(cleaner_down[1], c-1):
        # 왼쪽
        cleaned_mat[r-1][j] = next_mat[r-1][j+1]
    for i in range(cleaner_down[0]+1, r-1):
        # 위
        cleaned_mat[i][cleaner_down[1]] = next_mat[i+1][cleaner_down[1]]

    mat = cleaned_mat
    #print(next_mat)
    #print(cleaned_mat)
print(total)
