# 비요뜨의 징검다리 건너기
# 골드 5
# 분할 정복을 이용한 거듭제곱

# 처음과 마지막은 무조건 선택
# 중간 n-2개의 징검다리들을 선택하거나, 아니거나 2가지
# 2^(n-2)

import sys
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7


def power(n, x):
    # n^x
    if x == 0:
        return 1
    if x == 1:
        return n

    if x%2 == 0:
        return (power(n, x//2) ** 2) % MOD
    else:
        return ((power(n, x//2) ** 2) * n) % MOD


t = int(input())
for _ in range(t):
    m = int(input())
    if m == 1:
        print(1)
    else:
        print(power(2, m-2))
