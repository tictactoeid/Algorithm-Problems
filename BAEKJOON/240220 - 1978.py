# 소수 찾기 - 백준 #1978
# 브론즈 2

count = 0
n = int(input())
numbers = list(map(int, input().split()))

flag = False

for i in range(n): # i-th input number
    flag = False
    for j in range(2, numbers[i]): # 에라토스테네스의 체
        if (numbers[i] % j == 0):

            flag = True
            break
    if ((not flag) and numbers[i] > 1):
        count += 1

print(count)