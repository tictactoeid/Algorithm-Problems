# 헌내기는 친구가 필요해
# 실버 2

import sys
sys.setrecursionlimit(10**6)

visited = set()
start = (0, 0)

n, m = map(int, input().split())
campus = ["O" for _ in range(n)]

for i in range(n):
    line = input()
    campus[i] = line
    if "I" in line:
        start = (i, line.index("I"))


def neighbors(node):
    result = []
    if node[0] > 0:
        if campus[node[0]-1][node[1]] != 'X':
            result.append((node[0]-1, node[1]))
    if node[0] < n-1:
        if campus[node[0]+1][node[1]] != 'X':
            result.append((node[0]+1, node[1]))
    if node[1] > 0:
        if campus[node[0]][node[1]-1] != 'X':
            result.append((node[0], node[1] - 1))
    if node[1] < m-1:
        if campus[node[0]][node[1]+1] != 'X':
            result.append((node[0], node[1] + 1))

    return result


count = 0


def dfs(node):
    global count

    visited.add(node)
    if campus[node[0]][node[1]] == 'P':
        count += 1

    for neighbor in neighbors(node):
        if neighbor not in visited:
            dfs(neighbor)


dfs(start)
print(count) if count != 0 else print('TT')
#print(start)
#print(neighbors(start))


