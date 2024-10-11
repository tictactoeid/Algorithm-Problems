# 동전
# 골드 5

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [[0 for _ in range(target+1)] for _ in range(n)]

    k = 0
    while k <= target+1:
        dp[0][coins[0] * k] += 1

    for i in range(1, n):
        for w in range(target+1):
            if w >= coins[i]:
                dp[i][w] = dp[i-1][w] + dp[i-1][w-coins[i]]
            else:
                dp[i][w] = dp[i - 1][w]

    print(dp)
    print(dp[n-1][target])
