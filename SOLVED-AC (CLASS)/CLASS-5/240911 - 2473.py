# 세 용액
# 골드 3

# 이분 탐색: O(n^2 log n)
# Pypy로 통과

import bisect, math

n = int(input())
liquids = list(map(int, input().split()))


def sol(n, liquids):
    liquids.sort()
    result = [math.inf, None, None, None]
    for i in range(n):
        for j in range(i+1, n):
            l1 = liquids[i]
            l2 = liquids[j]
            target = 0 - l1 - l2
            idx = bisect.bisect_right(liquids, target)
            for k in range(idx-1, idx+2):
                if i == k or j == k:
                    continue
                if 0 <= k < n:
                    tmp = liquids[k]
                    value = l1 + l2 + tmp
                    if abs(value) < abs(result[0]):
                        result[0] = value
                        result[1:] = sorted([l1, l2, tmp])
                    if value == 0:
                        print(result[1], result[2], result[3])
                        return

    print(result[1], result[2], result[3])


sol(n, liquids)
