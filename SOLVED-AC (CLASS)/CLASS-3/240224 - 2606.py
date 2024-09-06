# 바이러스
# 실버 3

n = int(input())  # number of computers
k = int(input())  # number of edges

matrix = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(k):
    com1, com2 = map(int, input().split())
    matrix[com1 - 1][com2 - 1] = 1
    matrix[com2 - 1][com1 - 1] = 1


def search(node):
    # dfs
    visited[node] = 1
    for i in range(n):
        if node == i:
            continue
        if visited[i] == 0 and matrix[node][i] == 1:
            # connected and not visited yet
            search(i)


search(0)
print(sum(visited)-1) # exclude computer 1

