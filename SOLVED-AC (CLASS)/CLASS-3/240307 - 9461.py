# 파도반 수열
# 실버 3

t = int(input())
p = [0 for _ in range(100)]

p[0:10] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, 100):
    p[i] = p[i-1] + p[i-5]


for _ in range(t):
    n = int(input())
    print(p[n-1])
