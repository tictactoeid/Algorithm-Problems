# Four Squares
# 실버 3

# brute force
import sys

n = int(input())

tmp = n ** 0.5
for i in range(int(tmp)-2, int(tmp)+3):
    if i**2 == n:
        print(1)
        sys.exit()


minimum = 4
tmp = int(tmp) + 2
for i in range(1, tmp):
    for j in range(i, tmp):
        if i**2 + j**2 == n:
            print(2)
            sys.exit()
        for k in range(j, tmp):
            if i**2 + j**2 + k**2 == n:
                minimum = 3
print(minimum)