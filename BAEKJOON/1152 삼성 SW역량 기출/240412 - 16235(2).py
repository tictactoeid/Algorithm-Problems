# 나무 재테크
# 골드 3
# deque 이용 - 오히려 시간이 더 늘었음?
# Pypy3으로만 통과
from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().split())
mat = [[5 for _ in range(n)] for _ in range(n)]
s2d2 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

tree = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x-1][y-1].append(z)


def spring_summer():
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) == 0:
                continue


            new = deque()
            tmp = 0
            while tree[i][j]:
                age = tree[i][j].popleft()
                if mat[i][j] >= age:
                    mat[i][j] -= age
                    new.append(age + 1)
                else:
                    tmp += age // 2

            mat[i][j] += tmp
            tree[i][j] = new


def fall_winter():
    for i in range(n):
        for j in range(n):
            for t in tree[i][j]:
                if t % 5 == 0:
                    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                    for ne in neighbors:
                        if 0 <= ne[0] < n and 0 <= ne[1] < n:
                            tree[ne[0]][ne[1]].appendleft(1)
            mat[i][j] += s2d2[i][j]



for year in range(k):
    spring_summer()
    fall_winter()

result = 0
for i in range(n):
    for j in range(n):
        result += len(tree[i][j])

print(result)