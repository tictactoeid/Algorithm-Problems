# 키 순서
# 골드 4
# 재활훈련 - dfs

n, m = map(int, input().split())

mat = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1


longer = 0
shorter = 0
visited_longer = [False for _ in range(n)]
visited_shorter = [False for _ in range(n)]


def dfs_init():
    global longer, shorter, visited_longer, visited_shorter
    longer = 0
    shorter = 0
    visited_longer = [False for _ in range(n)]
    visited_shorter = [False for _ in range(n)]


def dfs_longer(node):
    global longer

    for i in range(n):
        if mat[i][node] and not visited_longer[i]:
            longer += 1
            visited_longer[i] = True
            dfs_longer(i)


def dfs_shorter(node):
    global shorter

    for i in range(n):
        if mat[node][i] and not visited_shorter[i]:
            shorter += 1
            visited_shorter[i] = True
            dfs_shorter(i)


cnt = 0
for i in range(n):
    dfs_init()
    dfs_longer(i)
    dfs_shorter(i)
    if longer + shorter == n-1:
        cnt += 1

print(cnt)
