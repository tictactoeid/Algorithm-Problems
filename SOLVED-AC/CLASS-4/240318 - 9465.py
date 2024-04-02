# 스티커
# 실버 1

t = int(input())

for _ in range(t):
    n = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    sticker = [line1, line2]
    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    result = max(dp[0][0], dp[1][0])

    if n == 1:
        print(result)
        continue

    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]
    result = max(result, dp[0][1], dp[1][1])

    for j in range(2, n):
        for i in range(2):
            dp[i][j] = max(dp[1-i][j-1], dp[i][j-2], dp[1-i][j-2]) + sticker[i][j]
            result = max(result, dp[i][j])
    #print(dp)
    print(result)
