# 팰린드롬?
# 골드 4

import sys

n = int(input())
sequence = list(map(int, input().split()))

m = int(input())
questions = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[False for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][i] = True


for start in range(n-1, 0, -1):
    for end in range(start+1, n+1):
        if end - start == 1:
            #print(start, end)
            if sequence[start-1] == sequence[end-1]:
                dp[start][end] = True
        #elif (end - start) % 2 == 0:  # 1, 2, 1
        if sequence[start-1] == sequence[end-1] and dp[start+1][end-1]:
            dp[start][end] = True
        #else:  # 1, 2, 2, 1

#print(dp)
for question in questions:
    start, end = question
    print(int(dp[start][end]))
