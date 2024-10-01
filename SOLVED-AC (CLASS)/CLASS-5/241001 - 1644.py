# 소수의 연속합
# 골드 3

import sys

n = int(input())

if n == 1:
    print(0)
    sys.exit()
elif n == 2:
    print(1)
    sys.exit()

# 에라토스테네스의 체 이용
# n 이하 소수를 얻음

is_prime = [True for _ in range(n+1)]

is_prime[0] = False
is_prime[1] = False

for i in range(2, n+1):
    if not is_prime[i]:
        continue
    j = 2
    while i * j <= n:
        is_prime[i*j] = False
        j += 1

primes = []
for i in range(2, n+1):
    if is_prime[i]:
        primes.append(i)

# print(is_prime)
# print(primes)
start = 0
end = 1
count = 0

current_sum = sum(primes[start:end])

while start < end and end <= len(primes):
    if current_sum > n:
        current_sum -= primes[start]
        start += 1
    elif current_sum == n:
        count += 1
        current_sum -= primes[start]
        start += 1
    else:
        if end == len(primes):
            break
        current_sum += primes[end]
        end += 1

print(start, end)
print(count)
