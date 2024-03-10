# AC
# 골드 5

from collections import deque

t = int(input())

for _ in range(t):
    flag = False
    p = input()
    n = int(input())
    q = deque(input().strip('[]').split(','))
    if n == 0:
        q = deque()
    isReversed = False

    for i in range(len(p)):
        if p[i] == 'R':
            isReversed = not isReversed
        elif p[i] == 'D':
            if len(q) == 0:
                print('error')
                flag = True
                break
            else:
                if isReversed:
                    q.pop()
                else:
                    q.popleft()


    if not flag:
        output = '['
        while len(q) > 0:
            if isReversed:
                output += str(q.pop())
            else:
                output += str(q.popleft())
            if len(q) >= 1:
                output += ','
        output += ']'
        print(output)