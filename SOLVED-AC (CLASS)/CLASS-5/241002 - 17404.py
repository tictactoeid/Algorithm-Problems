# RGB거리 2
# 골드 4

import math

n = int(input())
cost = [[] for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]

result = math.inf

for i in range(n):
    line = list(map(int, input().split()))
    cost[i] = line


for zero_color in range(3):
    dp[0] = [math.inf, math.inf, math.inf]
    dp[0][zero_color] = cost[0][zero_color]

    for i in range(1, n - 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]  # RED
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]  # GREEN
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]  # BLUE

    if zero_color == 0:
        dp[n-1][0] = math.inf
        dp[n-1][1] = min(dp[n-2][0], dp[n-2][2]) + cost[n-1][1]  # GREEN
        dp[n-1][2] = min(dp[n-2][0], dp[n-2][1]) + cost[n-1][2]  # BLUE
    elif zero_color == 1:
        dp[n-1][0] = min(dp[n-2][1], dp[n-2][2]) + cost[n-1][0]
        dp[n-1][1] = math.inf
        dp[n-1][2] = min(dp[n-2][0], dp[n-2][1]) + cost[n-1][2]  # BLUE
    if zero_color == 2:
        dp[n-1][0] = min(dp[n-2][1], dp[n-2][2]) + cost[n-1][0]
        dp[n-1][1] = min(dp[n-2][0], dp[n-2][2]) + cost[n-1][1]  # GREEN
        dp[n-1][2] = math.inf

    result = min(result, min(dp[n-1]))
    #print(dp)
print(result)

# 40 57 13
