# N-Queen
# 골드 4

n = int(input())

queens = [-1 for _ in range(n)] # rows
#cols = [-1 for _ in range(n)]
count = 0

def check(node):
    for i in range(node[0]):
        #if queen[0] == node[0]:
        #    return False
        if queens[i] == node[1]:
            return False
        if abs(i - node[0]) == abs(queens[i] - node[1]):
            return False
    return True


def dfs(node): # 백트래킹
    global count
    #if not check(node):
        #return
    queens[node[0]] = node[1]
    if queens[n-1] >= 0:
        count += 1
        #print(queens)
        return
    if node[0] + 1 >= n:
        return
    for i in range(n):
        next = (node[0] + 1, i)
        if check(next):
            dfs(next)
            queens[next[0]] = -1


for i in range(n):
    dfs((0, i))
    queens = [-1 for _ in range(n)]
print(count)


