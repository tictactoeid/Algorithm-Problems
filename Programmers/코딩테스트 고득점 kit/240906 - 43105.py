# 정수 삼각형
# 레벨 3
# 다이나믹 프로그래밍


# 쉬운데?

def solution(triangle):
    dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(i+1):
            # dp[i][j] <- dp[i-1][j] dp[i-1][j-1]
            if j - 1 >= 0 and j < i:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
    #print(dp)
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
print(solution([[100]]))
print(solution([[10], [20, 30]]))