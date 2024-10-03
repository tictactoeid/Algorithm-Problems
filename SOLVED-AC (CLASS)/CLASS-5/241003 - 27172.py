# 수 나누기 게임
# 골드 4

n = int(input())
lst = list(map(int, input().split()))
score = {}

for x in lst:
    score[x] = 0

for x in lst:
    n = 2
    while x*n <= 1000000:
        if x*n in score.keys():
            score[x*n] -= 1
            score[x] += 1
        n += 1

for x in lst:
    print(score[x], end=' ')
