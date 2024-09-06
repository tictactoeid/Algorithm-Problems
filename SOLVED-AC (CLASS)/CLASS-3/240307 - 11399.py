# ATM
# 실버 4

n = int(input())
p = list(map(int, input().split()))

p.sort()
summ = [sum(p[:i]) for i in range(1, len(p)+1)]
print(sum(summ))
