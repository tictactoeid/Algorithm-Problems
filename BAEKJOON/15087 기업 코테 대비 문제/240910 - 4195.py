# 친구 네트워크
# 골드 2

import sys
sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline())

parents = {}


# children을 set으로 관리 + find 함수에서 parent[]를 줄여가며 재귀적으로 최적화
# 2가지 수행하려다가 괜히 어려워진 문제
# find에서 최적화 X + children은 개수만 세기
# -> 시간 초과 발생하여, find 최적화 다시 수행


def union(a, b):
    global parents, count
    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        return
    else:
        parents[parent_b] = parent_a
        count[parent_a] += count[parent_b]


def find(a):
    global parents
    if parents[a] == -1:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]


for _ in range(t):
    f = int(sys.stdin.readline())
    parents = {}
    count = {}
    for _ in range(f):
        person1, person2 = sys.stdin.readline().split()
        if person1 not in parents.keys():
            parents[person1] = -1
            count[person1] = 1
        if person2 not in parents.keys():
            parents[person2] = -1
            count[person2] = 1

        union(person1, person2)
        print(count[find(person1)])

