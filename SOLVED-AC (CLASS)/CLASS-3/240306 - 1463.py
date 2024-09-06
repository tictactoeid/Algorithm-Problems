# 1로 만들기
# 실버 3

n = int(input())

memoization = [0 for _ in range(n)]
memoization[0] = 0
if n > 1:
    memoization[1] = 1
if n > 2:
    memoization[2] = 1

for i in range(3, n):
    num = i + 1
    if num % 6 == 0:
        memoization[i] = min(memoization[i//3], memoization[i//2], memoization[i-1]) + 1
    elif num % 3 == 0:
        memoization[i] = min(memoization[i // 3], memoization[i - 1]) + 1
    elif num % 2 == 0:
        memoization[i] = min(memoization[i // 2], memoization[i - 1]) + 1
    else:
        memoization[i] = memoization[i-1] + 1

print(memoization[n-1])