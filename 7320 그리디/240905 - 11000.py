# 강의실 배정
# 골드 5

import sys
import heapq

n = int(input())

classes = [() for _ in range(n)]
classrooms = []  # 각 강의실의 마지막 수업을 저장하는 heapq.

for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    classes[i] = (s, t)

classes.sort(key=lambda x: (x[0], x[1]))
# 먼저 "시작"하는 순서대로 정렬해야

classrooms = []

for c in classes:
    if classrooms and classrooms[0] <= c[0]:
        # 여기서 heap의 min값 비교 1번만으로 끝낼 수 있음
        heapq.heappop(classrooms)
    heapq.heappush(classrooms, c[1])

print(len(classrooms))
