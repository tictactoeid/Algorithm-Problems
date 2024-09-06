# 집합
# 실버 5

import sys
# sys.stdin.readline().rstrip()

m = int(sys.stdin.readline().rstrip())

S = set()

for _ in range(m):
    x = sys.stdin.readline().rstrip()
    if x == "all":
        S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif x == "empty":
        S = set()
    else:
        a, b = x.split()
        if a == "add":
            if int(b) not in S:
                S.add(int(b))
        elif a == "remove":
            if int(b) in S:
                S.remove(int(b))
        elif a == "check":
            if int(b) in S:
                sys.stdout.write("1\n")
            else:
                sys.stdout.write("0\n")
        elif a == "toggle":
            if int(b) in S:
                S.remove(int(b))
            else:
                S.add(int(b))