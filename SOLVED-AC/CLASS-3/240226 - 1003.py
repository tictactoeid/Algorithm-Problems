# 피보나치 함수
# 실버 3


t = int(input())
n = [0 for _ in range(t)]
for i in range(t):
    n[i] = int(input())

fibo = [[0, 0] for _ in range(max(n) + 1)]
fibo[0] = [1, 0]
if (max(n) > 0):
    fibo[1] = [0, 1]

for i in range(2, max(n)+1):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

for i in range(t):
    print("{0} {1}".format(fibo[n[i]][0], fibo[n[i]][1]))
