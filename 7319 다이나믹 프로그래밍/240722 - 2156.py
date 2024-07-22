# 포도주 시식
# 실버 1

n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]

# dp[i][k]: i까지, 연속 k잔 "이하"

dp[0][0] = 0
dp[0][1] = wine[0]
dp[0][2] = wine[0]

if n > 1:
    dp[1][0] = wine[0]
    dp[1][1] = max(wine[0], wine[1])
    dp[1][2] = wine[0] + wine[1]

    for i in range(2, n):
        dp[i][0] = max(dp[i-2])
        dp[i][1] = max(max(dp[i-1][0], max(dp[i-2])) + wine[i], dp[i-1][2], dp[i-1][1]) # , dp[i-1][1]
        dp[i][2] = max(dp[i-1][1], dp[i-1][0], max(dp[i-2])) + wine[i] # dp[i-1][0]

print(max(dp[n-1]))
#print(dp)
