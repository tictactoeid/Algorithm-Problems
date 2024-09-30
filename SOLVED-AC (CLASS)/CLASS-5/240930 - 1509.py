# 팰린드롬 분할
# 골드 1

# dp를 2번 쓰는 것이 핵심
# palindrome[][]: 보조용, 10942번 문제에서 가져옴
# dp[]: 문제의 메인 풀이
# 앞에서부터 그리디하게 자르면 최소임을 보장할 수 없으므로 dp[]로 체크

import math

string = input()
n = len(string)

palindrome = [[False for _ in range(n)] for _ in range(n)]
# palindrome[i][j]: string[i:j+1]이 palindrome?
# i > j인 경우 쓰레기 값

for i in range(n):
    palindrome[i][i] = True

for start in range(n-1, -1, -1):
    for end in range(start+1, n):
        if end - start == 1:
            if string[start] == string[end]:
                palindrome[start][end] = True
        elif string[start] == string[end] and palindrome[start+1][end-1]:
            palindrome[start][end] = True


dp = [math.inf for _ in range(n)]

# dp[i] : string[:i+1] 까지 팰린드롬 분할한 개수의 최솟값

dp[0] = 1

for end in range(1, n):
    for start in range(0, end+1):
        if palindrome[start][end]:
            if start == 0:
                dp[end] = min(dp[end], 1)
            else:
                dp[end] = min(dp[end], dp[start-1] + 1)

print(dp[n-1])
