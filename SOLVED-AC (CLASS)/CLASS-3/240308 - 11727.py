# 2*n 타일링 2
# 실버 3

n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = 1
if n >= 2:
    dp[2] = 3

for i in range(3, n+1):
    dp[i] = 2*dp[i-2] + dp[i-1]
            # 2*1 2*1 i-2, 2*2 i-2, 1*2 i-1
print(dp[n] % 10007)
