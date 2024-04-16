# 마법사 상어와 블리자드
# 골드 1

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
num = [() for _ in range(n**2)] # num[i]는 i번째 칸의 좌표 tuple을 저장

r, c = n//2, n//2
length = 1
count = 0
direction = 0 # 0 왼쪽, 1 아래, 2 오른쪽, 3 위쪽
for i in range(n**2):
    num[i] = (r, c)
    if direction == 0:
        c -= 1
    elif direction == 1:
        r += 1
    elif direction == 2:
        c += 1
    else:
        r -= 1
    count += 1
    if count == length:
        direction = (direction + 1) % 4
    elif count == 2*length:
        direction = (direction + 1) % 4
        count = 0
        if length != n-1:
            length += 1
#print(num)
exploded = [0, 0, 0]


def move():
    # 2번 연속 빈칸이면

    q = deque()
    for i in range(1, n**2):
        x = num[i][0]
        y = num[i][1]
        if mat[x][y] != 0:
            q.append(mat[x][y])

    for i in range(1, n**2):
        x = num[i][0]
        y = num[i][1]
        if q:
            mat[x][y] = q.popleft()
        else:
            mat[x][y] = 0


def explode(start, end, exploded):
    # TODO: q로 변경
    if end - start + 1 < 4:
        return exploded

    marble = mat[num[start][0]][num[start][1]]
    for i in range(start, end+1):
        x = num[i][0]
        y = num[i][1]
        mat[x][y] = 0
    count = end - start + 1
    exploded[marble-1] += count
    return exploded


def explode_search(exploded):
    # TODO: q로 변경
    start = 2
    end = 2
    curr = mat[num[1][0]][num[1][1]]
    flag = False
    for i in range(2, n**2):
        x = num[i][0]
        y = num[i][1]
        # if mat[x][y] == 0:
        #     print(x, y)
        #     return explode(start, end, exploded)
        if curr != mat[x][y] and curr != 0:
            if end - start + 1 >= 4:
                exploded = explode(start, end, exploded)
                flag = True
            curr = mat[x][y]
            start = i
            end = i
        else:
            end = i
            if i == n**2 - 1:
                if end - start + 1 >= 4 and curr != 0:
                    exploded = explode(start, end, exploded)
                    flag = True
    if not flag:
        return exploded
    else:
        move()
        return explode_search(exploded)


def change():
    q = deque()
    start = 1
    end = 1
    marble = mat[num[1][0]][num[1][1]]
    for i in range(2, n**2):
        x = num[i][0]
        y = num[i][1]
        #if mat[x][y] != 0:
        if True:
            if marble == mat[x][y]:
                end += 1
                if i == n**2 - 1 and marble != 0:
                    q.append(end - start + 1)
                    q.append(marble)
                    print(end - start + 1, marble)
            else:
                if marble != 0:
                    q.append(end - start + 1)
                    q.append(marble)
                    #print(end - start + 1, marble)
                marble = mat[x][y]
                start = i
                end = i
                if i == n**2 - 1 and marble != 0:
                    q.append(end - start + 1)
                    q.append(marble)
                    #print(end - start + 1, marble)


    for i in range(1, n**2):
        x = num[i][0]
        y = num[i][1]
        if q:
            mat[x][y] = q.popleft()
        else:
            mat[x][y] = 0


exploded = [0, 0, 0]
for i in range(m):
    d, s = map(int, input().split())
    dx = 0
    dy = 0
    if d == 1: # 위
        dx -= 1
    elif d == 2: # 아래
        dx += 1
    elif d == 3: # 왼
        dy -= 1
    else: # 오른
        dy += 1

    x = n//2
    y = n//2
    for _ in range(s):
        x += dx
        y += dy
        mat[x][y] = 0
    #print(mat)
    move()
    #print("블-이")
    #print(mat)
    exploded = explode_search(exploded)
    #print("폭")
    #print(mat)
    move()
    #print("이")
    #print(mat)
    change()
    #print("변")
    #print(mat)
    print(mat)
    # TODO

print(1*exploded[0] + 2*exploded[1] + 3*exploded[2])

print(num)