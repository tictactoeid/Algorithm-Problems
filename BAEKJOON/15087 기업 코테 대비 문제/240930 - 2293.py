# 동전 1
# 골드 4

n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]  # dp[i]: 동전 가치의 합이 i원이 되는 경우의 수
dp[0] = 1  # 동전을 쓰지 않고 0원을 만드는 것도 하나의 방법

coins = sorted([int(input()) for _ in range(n)])


for coin in coins:
    for money in range(1, k + 1):
        if money >= coin:
            dp[money] += dp[money - coin]
            # 1, 2, 5원 동전으로 10원을 만든다면
            # 1원 하나 + 여러 개로 9원
            # 2원 하나 + 여러 개로 2원
            # 5원 하나 + 여러 개로 5원

print(dp[k])
