# 인구 이동
# 골드 4

n, l, r = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

parent = [[(i, j) for j in range(n)] for i in range(n)]


def find(i, j):
    if (i, j) == parent[i][j]:
        return (i, j)
    else:
        parent[i][j] = find(parent[i][j][0], parent[i][j][1])
        return find(parent[i][j][0], parent[i][j][1])


def union(i1, j1, i2, j2):
    r1 = find(i1, j1)
    r2 = find(i2, j2)
    if r1 != r2:
        parent[i2][j2] = (i1, j1)


def reset():
    global parent
    parent = [[(i, j) for j in range(n)] for i in range(n)]


def check_and_union(i1, j1, i2, j2):
    flag = False
    if l <= abs(mat[i1][j1] - mat[i2][j2]) <= r:
        #print(mat[i1][j1], mat[i2][j2], i1, j1, i2, j2)
        union(i1, j1, i2, j2)
        flag = True
    return flag


def move():
    unions = [[[] for _ in range(n)] for _ in range(n)]
    flag = False
    #print("parent-first")
    #print(parent)
    for i in range(n):
        for j in range(n):
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for i1, j1 in neighbors:
                if 0 <= i1 < n and 0 <= j1 < n:
                    if check_and_union(i, j, i1, j1):
                        flag = True
                        print(i, j, i1, j1)
    #print("parent")
    #print(parent)
    for i in range(n):
        for j in range(n):
            x, y = find(i, j)
            #print(i, j, x, y)
            unions[x][y].append((i, j))
    for i in range(n):
        for j in range(n):
            length = len(unions[i][j])
            sum = 0
            if length > 1:
                for country in unions[i][j]:
                    sum += mat[country[0]][country[1]]
                sum = sum // length
                for country in unions[i][j]:
                    mat[country[0]][country[1]] = sum
    #print(unions)
    reset()

    print(mat)
    #print(flag)
    return flag


for t in range(2001):
    if not move():
        print(t)
        break