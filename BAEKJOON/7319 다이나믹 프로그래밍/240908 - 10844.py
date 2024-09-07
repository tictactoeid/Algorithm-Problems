# 쉬운 계단 수
# 실버 1

import sys

MOD = 1000000000

n = int(input())
if n == 1:
    print(9)
    sys.exit()

dp = [[0 for _ in range(10)] for _ in range(n+1)]

# dp[i][k]: i자리 계단수 중 k로 끝나는 것의 수

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD

print(sum(dp[n]) % 1000000000)
