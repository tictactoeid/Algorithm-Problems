# 나는야 포켓몬 마스터 이다솜
# 실버 4

import sys

n, m = map(int, sys.stdin.readline().split())

number_name = {}
name_number = {}

for i in range(n):
    name = sys.stdin.readline().strip()
    number_name[i+1] = name
    name_number[name] = i+1

for i in range(m):
    problem = sys.stdin.readline()
    problem = problem.strip()
    if problem.isdigit():
        print(number_name[int(problem)])
    else:
        print(name_number[problem])

