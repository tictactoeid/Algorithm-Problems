# 구간 합 구하기 5
# 실버 1
import sys

n, m = map(int, input().split())

matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for j in range(n):
    dp[0][j] = sum(matrix[0][:j+1])

for i in range(1, n):
    for j in range(0, n):
        dp[i][j] = dp[i-1][j] + sum(matrix[i][:j+1])

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 > 1 and y1 > 1:
        value = dp[x2-1][y2-1] - dp[x2-1][y1-2] - dp[x1-2][y2-1] + dp[x1-2][y1-2]
    elif x1 > 1:
        value = dp[x2-1][y2-1] - dp[x1-2][y2-1]
    elif y1 > 1:
        value = dp[x2-1][y2-1] - dp[x2-1][y1-2]
    else:
        value = dp[x2-1][y2-1]
    print(value)

