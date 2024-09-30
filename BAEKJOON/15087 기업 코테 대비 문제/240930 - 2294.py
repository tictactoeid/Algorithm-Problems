# 동전 2
# 골드 5

import math

n, k = map(int, input().split())

dp = [math.inf for _ in range(k+1)]  # dp[i]: 동전 가치의 합이 i원이 되는 경우의 수
dp[0] = 0

coins = sorted([int(input()) for _ in range(n)])

for coin in coins:
    for money in range(1, k + 1):
        if money >= coin:
            dp[money] = min(dp[money - coin] + 1, dp[money])

if dp[k] == math.inf:
    print(-1)
else:
    print(dp[k])
    