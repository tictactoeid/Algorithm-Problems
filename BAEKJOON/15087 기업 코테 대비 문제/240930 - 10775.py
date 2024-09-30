# 공항
# 골드 2

import sys

g = int(input())
p = int(input())

airplanes = [int(sys.stdin.readline()) for _ in range(p)]
parents = [-1 for _ in range(g+1)]


def find(x):
    if parents[x] == -1:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    parent1 = find(x)
    parent2 = find(y)

    if parent1 == parent2:
        return

    parents[parent2] = parent1


cnt = 0
for airplane in airplanes:
    target = find(airplane)
    if target == 0:  # 0번 (존재하지 않는) 게이트를 가리킴 -> 더 넣을 수 없음
        break

    cnt += 1
    union(target-1, target)

    # 예를 들어 7번 게이트에 비행기를 도킹한 경우
    # 6, 7이 union됨
    # 이후 7번 게이트에 도착한 비행기는 6번 게이트로 가야 함을 O(1)으로 구할 수 있음

print(cnt)
