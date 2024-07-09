# 오큰수
# 골드 4

from collections import deque


n = int(input())
a = list(map(int, input().split()))
stack = []
last = 0
result = [-1 for _ in range(n)]
for i in range(n):
    if not stack:
        stack.append((i, a[i]))
    else:
        if stack[-1][1] >= a[i]: # stack의 top value
            stack.append((i, a[i]))
        else:
            # update result
            while stack:
                if stack[-1][1] < a[i]:
                    result[stack[-1][0]] = a[i]
                    stack.pop()
                else:
                    break
            stack.append((i, a[i]))

for j in range(n):
    print(result[j], end=' ')


