# 가장 긴 바이토닉 부분 수열
# 골드 4

n = int(input())
dp = [[1, 1, 1] for _ in range(n)]
# 증가, 감소, 증가하다 감소
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1):
        if a[j] < a[i]: # 증가
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif a[j] > a[i]: # 감소
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
            dp[i][2] = max(dp[i][2], dp[j][0] + 1, dp[j][2] + 1)
            # 기존 값, 증가하다가 이번에 처음 감소, 증가하다가 (이미 꺾여서) 감소 중

result = 0
for i in range(n):
    result = max(result, max(dp[i]))
print(result)