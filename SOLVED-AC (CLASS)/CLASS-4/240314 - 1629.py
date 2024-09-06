# 곱셈
# 실버 1

# 분할 정복을 이용한 거듭제곱
# x^n = x^n/2 * x^n/2 ( x%2 == 0)
# x^n = x^n//2 * x^n//2 * x ( x%2 == 1)
# O(log n)

a, b, c = map(int, input().split())

def power(a, b, c):
    if b == 1: # base case
        return a%c
    else:
        if b % 2 == 0:
            return power(a%c, b//2, c) ** 2 % c
        else:
            return power(a%c, b//2, c) ** 2 * a % c

print(power(a, b, c))