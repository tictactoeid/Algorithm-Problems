# 계단 수
# 골드 1

n = int(input())

if n < 10:
    print(0)
else:
    DIVISOR = 1000000000
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    dp[10][0] = 1 # 0123456789
    dp[10][9] = 1 # 9876543210
    # dp[n][i]: i로 시작하는, 길이 n의 계단수

    for i in range(11, n+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]

        for j in range(1, 9):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % DIVISOR

    print(dp[n-1])
    print(dp[n])
    print(sum(dp[n][1:]) % DIVISOR)


