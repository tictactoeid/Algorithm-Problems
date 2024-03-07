# 패션왕 신해빈
# 실버 3

cases = int(input())

for _ in range(cases):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in clothes.keys():
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1
    count -= 1
    print(count)

