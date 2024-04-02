# 파이프 옮기기 1
# 골드 5

n = int(input())
mat = [[] for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
# 가로 세로 대각선

for i in range(n):
    mat[i] = list(map(int, input().split()))

for i in range(1, n):
    if mat[0][i] == 1:
        break
    dp[0][i][0] = 1

for i in range(1, n): # 첫 줄은 다 채워놨음
    for j in range(1, n): # (0, 0), (0, 1) 로부터 시작, 1행은 어차피 못 감
        if mat[i][j] == 1:
            dp[i][j] = [0, 0, 0] # 벽
        else:
            dp[i][j][0] += (dp[i][j-1][0] + dp[i][j-1][2])
            dp[i][j][1] += (dp[i-1][j][1] + dp[i-1][j][2])
            if mat[i-1][j] != 1 and mat[i][j-1] != 1:
                dp[i][j][2] += sum(dp[i-1][j-1])

#print(dp)
print(sum(dp[n-1][n-1]))