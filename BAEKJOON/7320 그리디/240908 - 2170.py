# 선 긋기
# 골드 5

import sys

n = int(input())

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lines.sort()

length = lines[0][1] - lines[0][0]
last_end = lines[0][1]

for i in range(1, len(lines)):
    if last_end <= lines[i][0]:
        length += lines[i][1] - lines[i][0]
    else:
        tmp = lines[i][1] - last_end
        if tmp >= 0:
            length += tmp
    last_end = max(last_end, lines[i][1])

print(length)


# 빠른 입출력 (sys.stdin.readline()) 사용하여 Python3로도 통과
# last_end를 계속 갱신해줘야 함. 단순히 직전 선의 끝을 비교하는 것으로는 안 됨.
# ex) 1 3 / 2 5 / 3 4
