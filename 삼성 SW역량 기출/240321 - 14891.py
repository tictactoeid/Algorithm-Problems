# 톱니바퀴
# 골드 5
from collections import deque

wheels = [deque() for _ in range(4)]

for i in range(4):
    line = map(int, input())
    for j in line:
        wheels[i].append(j)


isRotated = [False, False, False, False]
def rotate(num, isClockwise):
    global isRotated
    if isRotated[num]:
        return
    isRotated[num] = True

    if num - 1 >= 0:
        if wheels[num][6] != wheels[num-1][2]:
            rotate(num-1, 1 - isClockwise)
    if num + 1 < 4:
        if wheels[num+1][6] != wheels[num][2]:
            rotate(num+1, 1 - isClockwise)

    if isClockwise > 0:
        tmp = wheels[num].pop()
        wheels[num].appendleft(tmp)
    else:
        tmp = wheels[num].popleft()
        wheels[num].append(tmp)


k = int(input())
for _ in range(k):
    isRotated = [False, False, False, False]
    num, isClockwise = map(int, input().split())
    rotate(num - 1, isClockwise)
# print(wheels[0])
# print(wheels[1])
# print(wheels[2])
# print(wheels[3])
# print(isRotated)
print(1*wheels[0][0] + 2*wheels[1][0] + 4*wheels[2][0] + 8*wheels[3][0])
