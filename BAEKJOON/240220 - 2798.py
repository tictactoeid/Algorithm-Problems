# 블랙잭
# 브론즈 2
n, m = map(int, input().split())  # 5 21
cards = list(map(int, input().split()))  # 5 6 7 8 9
result = [-1, -1, -1]


def currentSum():
    return result[0] + result[1] + result[2]


for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            current = cards[i] + cards[j] + cards[k]
            if current > m:
                continue
            if current > currentSum():
                result = [cards[i], cards[j], cards[k]]

print(currentSum())
