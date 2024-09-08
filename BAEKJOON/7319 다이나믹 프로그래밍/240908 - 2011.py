# 암호코드
# 골드 5

import sys

password = input()

if password[0] == '0':
    print(0)
    sys.exit()
elif len(password) == 1:
    print(1)
    sys.exit()


def two_digit_to_int(i):
    if i+1 < len(password):
        return int(password[i:i+2])


dp = [0 for _ in range(len(password) + 1)]

dp[0] = 1
dp[1] = 1

for i in range(2, len(password) + 1):
    if 1 <= int(password[i-1]) <= 9:
        dp[i] += dp[i-1] % 1000000

    if 10 <= two_digit_to_int(i-2) <= 26:
        dp[i] += dp[i-2] % 1000000

print(dp[len(password)] % 1000000)
#print(dp)
