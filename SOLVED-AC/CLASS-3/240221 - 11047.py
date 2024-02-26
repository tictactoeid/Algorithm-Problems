# 동전 0
# 실버 4

n, k = map(int, input().split())
coins = []
count = 0
money = k
for _ in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    count += int(money / coins[i])
    money -= int(money / coins[i]) * coins[i]

print(count)