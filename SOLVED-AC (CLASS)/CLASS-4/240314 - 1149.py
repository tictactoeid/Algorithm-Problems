# RGB거리
# 실버 1

n = int(input())
cost = [[] for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    cost[i] = line

dp[0] = cost[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0] # RED
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1] # GREEN
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))
