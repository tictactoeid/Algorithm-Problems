# 1, 2, 3 더하기
# 실버 3

T = int(input())

a = [0 for _ in range(10)]
# order matters
a[0] = 1 # 1
a[1] = 2 # 2 11
a[2] = 4 # 3 21 12 111

for i in range(3, 10):
    a[i] = a[i-1] + a[i-2] + a[i-3]

for _ in range(T):
    n = int(input())
    print(a[n-1])