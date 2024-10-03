# 피리 부는 사나이
# 골드 3

n, m = map(int, input().split())

mat = [input() for _ in range(n)]

parents = [[(i, j) for j in range(m)] for i in range(n)]


def find(i, j):
    if parents[i][j] == (i, j):
        return (i, j)
    else:
        x, y = parents[i][j]
        parents[i][j] = find(x, y)
        return parents[i][j]


def union(i1, j1, i2, j2):
    x1, y1 = find(i1, j1)
    x2, y2 = find(i2, j2)

    if (x1, y1) == (x2, y2):
        return
    parents[x2][y2] = (x1, y1)


for i in range(n):
    for j in range(m):
        if mat[i][j] == "U":
            union(i-1, j, i, j)
        elif mat[i][j] == "D":
            union(i+1, j, i, j)
        elif mat[i][j] == "L":
            union(i, j-1, i, j)
        else:
            union(i, j+1, i, j)


count = 0
for i in range(n):
    for j in range(m):
        if find(i, j) == (i, j):
            count += 1

print(count)
