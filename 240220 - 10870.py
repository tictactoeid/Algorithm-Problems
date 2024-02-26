# 피보나치 수 5 - 백준 #10870
# 브론즈 2

n = int(input())


def fibo(num):
    if (num == 0):
        return 0
    if (num == 1):
        return 1
    return fibo(num - 1) + fibo(num - 2)


print(fibo(n))
