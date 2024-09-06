# 수 묶기
# 골드 4

import sys

n = int(input())
sequence = [int(input()) for _ in range(n)]

if n == 1:
    print(sequence[0])
    sys.exit()

sequence.sort()


result = 0
tmp = (0, 0)

for i in range(0, len(sequence), 2):
    if i+1 >= len(sequence):
        result += sequence[i]
        tmp = (i, i)
        break

    first = sequence[i]
    second = sequence[i+1]

    if first > 0:
        tmp = (i-1, i-1)
        break

    if first <= 0 < second:
        # result += max(first*second, first+second)
        # tmp = (i, i+1) # 중복처리 로직
        break
    else:
        result += first*second

#print(sequence)
#print(result, tmp)

for i in range(len(sequence)-1, -1, -2):
    if i-1 < 0:
        result += sequence[i]
        break

    first = sequence[i]
    second = sequence[i-1]

    if first <= 0:
        break

    if first > 0 >= second:
        # if i-1 == tmp[0] and i == tmp[1]:
        #     continue
        result += max(first*second, first+second)
    else:
        if first == second == 1:
            result += 2
        else:
            result += first * second

print(result)
# 5
# -5
# 0
# 0
# 1
# 2