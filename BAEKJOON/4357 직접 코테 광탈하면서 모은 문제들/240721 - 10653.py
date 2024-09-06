# 마라톤 2
# 골드 3
# 실패

import math

n, k = map(int, input().split())
checkpoints = [(0, 0) for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    checkpoints[i] = (x, y)


# def go_next_checkpoint(x, y, next_chk_num, passed_cnt, dist):
#     # base case
#     if next_chk_num == n:
#         return dist
#
#     # do not pass
#     next_x, next_y = checkpoints[next_chk_num]
#     curr_dist = abs(next_x - x) + abs(next_y - y)
#     #print(curr_dist)
#
#     if passed_cnt < k:
#         return min(go_next_checkpoint(next_x, next_y, next_chk_num+1, passed_cnt, dist+curr_dist), go_next_checkpoint(x, y, next_chk_num+1, passed_cnt+1, dist))
#     else:
#         return go_next_checkpoint(next_x, next_y, next_chk_num+1, passed_cnt, dist+curr_dist)
#
#
# x, y = checkpoints[0]
# print(go_next_checkpoint(x, y, 1, 0, 0))


dp = [[(math.inf, 0, 0) for _ in range(k+1)] for _ in range(n)]
# nth checkpoint, skipped k times

for i in range(k+1):
    dp[0][i] = (0, checkpoints[0][0], checkpoints[0][1])


def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def dp(n, k):


for i in range(1, n):
    for j in range(k+1):
        no_skip = dp[i - 1][j][0] + dist(dp[i - 1][j][1], dp[i - 1][j][2], checkpoints[i][0], checkpoints[i][1])
        #if j == 0 or i == n-1:
        if j == 0:
            #print(i, j)
            dp[i][j] = (no_skip, checkpoints[i][0], checkpoints[i][1])
            continue

        skip = dp[i-1][j-1][0]
        if skip < no_skip:
            dp[i][j] = (skip, dp[i-1][j-1][1], dp[i-1][j-1][2])
        else:
            dp[i][j] = (no_skip, checkpoints[i][0], checkpoints[i][1])

result = math.inf
for j in range(k+1):
    result = min(result, dp[n-1][j][0])

print(dp)
print(result)
#print(dp[n-1][k][0])

# 반례5 1
# # 0 0
# # 8 3
# # 1 1
# # 10 -5
# # 2 2
#