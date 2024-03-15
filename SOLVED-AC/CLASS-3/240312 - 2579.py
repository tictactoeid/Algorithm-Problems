# 계단 오르기
# 실버 3

n = int(input())

stairs = [0 for _ in range(n)]
for i in range(n):
    stairs[i] = int(input())

dp = [[0 for _ in range(2)] for _ in range(n)]

# dp[i][0] : 마지막으로 연속으로 1개 계단만 밟았을때 i에서의 max, 즉 i-1은 안 밟고 i는 밟은 경우
# dp[i][1] : 연속 2개

dp[0][0] = stairs[0]
dp[0][1] = stairs[0]

if n > 1:
    dp[1][0] = stairs[1]
    dp[1][1] = stairs[0] + stairs[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-2]) + stairs[i]
    dp[i][1] = dp[i-1][0] + stairs[i]

print(max(dp[n-1]))