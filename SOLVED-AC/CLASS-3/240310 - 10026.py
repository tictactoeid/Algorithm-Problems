# 적록색약
# 골드 5

import sys
sys.setrecursionlimit(10**6)

n = int(input())

matrix = ['' for _ in range(n)]
visited = set()
visited_blind = set()

for i in range(n):
    line = input()
    matrix[i] = line


def get_neighbors(node, isColorBlind):
    neighbors = []
    candidates = [(node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] - 1), (node[0], node[1] + 1)]

    color = matrix[node[0]][node[1]]
    RG = ['R', 'G']

    for candidate in candidates:
        if candidate[0] < 0 or candidate[1] < 0 or candidate[0] > n - 1 or candidate[1] > n - 1:
            continue
        color_candidate = matrix[candidate[0]][candidate[1]]
        if color_candidate == color:
            neighbors.append(candidate)
        elif isColorBlind and color in RG and color_candidate in RG:
            neighbors.append(candidate)
    return neighbors


def dfs(node, isColorBlind):
    if isColorBlind:
        visited_blind.add(node)
        for neighbor in get_neighbors(node, isColorBlind):
            if neighbor not in visited_blind:
                dfs(neighbor, isColorBlind)

    else:
        visited.add(node)
        for neighbor in get_neighbors(node, isColorBlind):
            if neighbor not in visited:
                dfs(neighbor, isColorBlind)


count = 0
count_blind = 0
for i in range(n):
    for j in range(n):
        node = (i, j)
        if node not in visited:
            count += 1
            dfs(node, False)

        if node not in visited_blind:
            count_blind += 1
            dfs(node, True)


print(count, count_blind)
