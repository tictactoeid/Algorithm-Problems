# 평범한 배낭
# 골드 5

# dp[i][w] : 최대무게가 w인 가방에서, i번째까지 판단했을 때 최대 가치

n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
weight = [0 for _ in range(n+1)]
value = [0 for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    weight[i] = w
    value[i] = v

for i in range(1, n+1):
    for w in range(1, k+1):
        if weight[i] <= w: # 담을 수 있는 경우
            dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])


