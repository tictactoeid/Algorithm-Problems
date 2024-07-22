# 1, 2, 3 더하기 3
# 실버 2

t = int(input())

dp = [0 for _ in range(1000001)]

dp[0] = 0
dp[1] = 1
dp[2] = 2 # 2, 1+1
dp[3] = 4 # 3, 2+1, 1+2, 1+1+1

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for _ in range(t):
    n = int(input())
    print(dp[n])
