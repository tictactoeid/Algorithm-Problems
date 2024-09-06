# 정수 삼각형
# 실버 1
import sys
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(i+1):
        tree[i][j] = line[j]

dp[0][0] = tree[0][0]
for i in range(n-1):
    for j in range(i+1):
        for k in range(j, j+2):
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + tree[i+1][k])




print(max(dp[n-1]))

