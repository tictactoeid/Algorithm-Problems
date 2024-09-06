# 옥상 정원 꾸미기
# 골드 5
import sys

n = int(sys.stdin.readline())
heights = [0 for _ in range(n)]
for i in range(n):
    heights[i] = int(sys.stdin.readline())

stack = []
count = 0

for i in range(n-1, -1, -1):
    print("stack: ", end='')
    for j in stack:
        print(heights[j], end=' ')
    print()
    idx = n
    while stack:
        if heights[stack[-1]] < heights[i]:
            stack.pop()
        else:
            idx = stack[-1] # 내가 볼 수 없는 첫 번째 건물
            print(heights[idx], heights[stack[-1]])
            count += (idx - i - 1)
            print((idx - i - 1))
            break
    stack.append(i)
    if not stack:

        print((idx-i-1))
        count += (idx-i-1)
print(count)


