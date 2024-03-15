# Four Squares
# 17626

# dp

# Pypy3

n = int(input())

tmp = int(n**0.5) + 1
dp = [4 for _ in range(n+1)]
dp[0] = 0
for i in range(1, tmp):
    dp[i**2] = 1

for i in range(1, n+1):
    if dp[i] == 1 or dp[i] == 2:
        continue
    for t in range(0, tmp):
        if 0 < i - t**2 <= n:
            dp[i] = min(dp[i - t**2] + 1, dp[i])
            if dp[i] == 1 or dp[i] == 2:
                break


print(dp[n])

