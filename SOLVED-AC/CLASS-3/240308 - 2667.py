# 단지번호붙이기
# 실버 1

n = int(input())

mat = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(n):
        if line[j] == '0':
            mat[i][j] = 0
        else:
            mat[i][j] = -1


def neighbors(node):
    neighbors = []
    if node[0] > 0:
        neighbors.append((node[0] - 1, node[1]))
    if node[0] < n-1:
        neighbors.append((node[0] + 1, node[1]))
    if node[1] > 0:
        neighbors.append((node[0], node[1] - 1))
    if node[1] < n-1:
        neighbors.append((node[0], node[1] + 1))
    return neighbors


group = 0
count = 0
result = []


def dfs(node, group_no):
    global count
    mat[node[0]][node[1]] = group_no # visited = True
    count += 1

    for neighbor in neighbors(node):
        if mat[neighbor[0]][neighbor[1]] < 0:
            dfs(neighbor, group_no)


for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            group += 1
            count = 0
            dfs((i, j), group)
            result.append(count)

print(group)
result.sort()
for i in result:
    print(i)