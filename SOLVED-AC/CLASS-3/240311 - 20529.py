# 가장 가까운 세 사람의 심리적 거리
# 실버 1
import math

t = int(input())


def distance(a, b):
    dist = 0
    for i in range(4):
        if a[i] != b[i]:
            dist += 1
    return dist


for _ in range(t):
    n = int(input())
    students = list(input().split())

    if n > 48:
        print(0)
    else:
        dist = math.inf
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    dist = min(dist, distance(students[i], students[j]) + distance(students[j], students[k]) + distance(students[k], students[i]))

        print(dist)
