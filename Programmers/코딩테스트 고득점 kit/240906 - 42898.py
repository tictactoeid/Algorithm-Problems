# 등굣길
# 레벨 3
# DP

def solution(m, n, puddles):
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for puddle in puddles:
        dp[puddle[0] - 1][puddle[1] - 1] = 0
    print(dp)
    if m > 1 and n > 1:
        for i in range(0, m):
            for j in range(0, n):
                if [i+1, j+1] in puddles:
                    dp[i][j] = 0
                else:
                    tmp = 0
                    if i >= 1:
                        tmp += dp[i-1][j]
                    if j >= 1:
                        tmp += dp[i][j-1]
                    if i >= 1 or j >= 1:
                        dp[i][j] = tmp % 1000000007
    else:
        if puddles:
            return 0
        else:
            return 1
    print(dp)
    return dp[m - 1][n - 1] % 1000000007

print(solution(4, 3, [[2, 2]]))
