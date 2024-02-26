# 좌표 압축
# 실버 2

n = int(input())
x = list(map(int, input().split()))
tmp = [[0, 0] for _ in range(n)]
result = [[0, 0] for _ in range(n)]
for i in range(n):
    tmp[i] = [i, x[i]] # index, coordinate

tmp.sort(key=lambda item: item[1]) # by coordinate


count = -1
prev = 10000000000
for i in range(n):
    if prev != tmp[i][1]: # unique
        count += 1
        prev = tmp[i][1]

    tmp[i][1] = count

tmp.sort(key=lambda item: item[0]) # by index
for i in range(n):
    print(tmp[i][1], end=" ")

