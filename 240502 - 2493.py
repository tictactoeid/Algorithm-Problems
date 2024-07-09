# 탑
# 골드 5

stack = []

n = int(input())

towers = list(map(int, input().split()))

for i in range(len(towers)):
    tower = towers[i]
    flag = False
    while stack:
        idx, height = stack.pop()
        if height >= tower:
            print(idx, end=' ')
            flag = True
            stack.append((idx, height))
            break
    if not flag:
        print(0, end=' ')
    stack.append((i+1, tower))
