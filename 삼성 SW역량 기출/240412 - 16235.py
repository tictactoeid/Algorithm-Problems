# 나무 재테크
# 골드 3

# Pypy3으로만 통과

n, m, k = map(int, input().split())
mat = [[5 for _ in range(n)] for _ in range(n)]
s2d2 = [list(map(int, input().split())) for _ in range(n)]

tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)


def spring_summer():
    #dead = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) == 0:
                continue

            if len(tree[i][j]) >= 2:
                tree[i][j].sort()

            tmp = 0
            dead = -1
            for t in range(len(tree[i][j])):
                age = tree[i][j][t]
                # print("Age", age)
                if mat[i][j] >= age:
                    mat[i][j] -= age
                    tree[i][j][t] += 1
                else:
                    dead = t
                    break
                    #dead.append(age)
                    #tmp += (age // 2)
                    #dead[i][j].append(age)

            if dead != -1:
                # print(tree[i][j])
                # print(dead)
                for t in tree[i][j][dead:]:
                    mat[i][j] += (t // 2)
                tree[i][j] = tree[i][j][:dead]
                # print(tree[i][j])
            # for d in dead:
            #     tree[i][j].remove(d)
            # mat[i][j] += tmp
    #return dead


def fall():
    for i in range(n):
        for j in range(n):
            for t in tree[i][j]:
                if t % 5 == 0:
                    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                    for ne in neighbors:
                        if 0 <= ne[0] < n and 0 <= ne[1] < n:
                            tree[ne[0]][ne[1]].append(1)


def winter():
    for i in range(n):
        for j in range(n):
            mat[i][j] += s2d2[i][j]


for year in range(k):
    #dead = spring()
    #summer(dead)
    spring_summer()
    fall()
    winter()
    # print(year, "tree")
    # for i in range(n):
    #     print(tree[i])
    # print(year, "mat")
    # for i in range(n):
    #     print(mat[i])

result = 0
for i in range(n):
    for j in range(n):
        result += len(tree[i][j])

print(result)