# 좋다
# 골드 4


# 완전 탐색: O(n^3)
# n = 2000이므로, O(n^3)는 무리, O(n^2 log n) 까지는 할 만 하다
# => 이중 for문 안에서 binary search

import bisect, sys


n = int(input())

numbers = list(map(int, input().split()))

if n <= 2:
    print(0)
    sys.exit()

numbers.sort()

count = 0
for i in range(n):
    for j in range(n):  # i까지가 아니라 n까지인 이유는 입력이 음수일 수도 있기 때문
        if i == j:
            continue

        flag = False
        target = numbers[i] - numbers[j]
        left = bisect.bisect_left(numbers, target)
        right = bisect.bisect_right(numbers, target)

        for k in range(left, right+1):
            if k != i and k != j and 0 <= k < n and target == numbers[k]:
                count += 1
                flag = True
                break
        if flag:
            break

print(count)
