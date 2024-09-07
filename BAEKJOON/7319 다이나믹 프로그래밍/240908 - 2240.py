# 자두나무
# 골드 5

t, w = map(int, input().split())

# dp = [[[0 for _ in range(2)] for _ in range(w+1)] for _ in range(t+1)]
#
# # dp[i][j][k]: i초에서, j번 움직였으며, 현재 k번 나무 밑에 있음
#
# # 자두는 무조건 0번 나무에서 시작
# current = int(input()) - 1
# if current == 0:
#     dp[1][0][current] = 1
# else:
#     dp[1][1][current] = 1
#
#
# for i in range(2, t+1):
#     current = int(input()) - 1
#
#     for j in range(0, w+1):
#         if j == w or j == 0:
#             # TODO: j==0인 경우 curr = 1일 수 없음,, 무조건 0 들어가야 함..
#             if j == 0 and current == 1:
#                 continue
#             dp[i][j][current] = dp[i-1][j][current] + 1
#         else:
#             dp[i][j][current] = max(dp[i-1][j][current], dp[i-1][j-1][1-current]) + 1
#         dp[i][j][1-current] = dp[i-1][j][1-current]
#
# print(dp)
# print(max(max(row) for row in dp[t]))

dp = [[0 for _ in range(w+1)] for _ in range(t+1)]

# dp[i][j]: i초, j번 이동
# j가 짝수이면 무조건 1번 나무 아래 있음
# j가 홀수이면 무조건 2번 나무 아래 있음

# 무조건 1번에서 시작하므로, 위 사항을 고려하여 dp를 새로 작성하여 해결

for i in range(1, t+1):
    jadu = int(input())
    for j in range(0, w+1):
        if j % 2 == 0:
            current = 1
        else:
            current = 2

        if jadu == current:
            if j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = dp[i - 1][j] + 1
        else:
            if j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
            else:
                dp[i][j] = dp[i - 1][j]

print(max(dp[t]))
