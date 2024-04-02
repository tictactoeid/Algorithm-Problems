# 내려가기
# 골드 5
import sys

n = int(input())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
for i in range(n): # 1줄씩 내려갈 때마다 dp를 갱신하고, 딱 그만큼만 갖고 있어야 4MB 안에서 풀 수 있다.
    # 슬라이딩 윈도우
    a, b, c = map(int, sys.stdin.readline().split())
    dp_max = [max(dp_max[0], dp_max[1])+a, max(dp_max)+b, max(dp_max[1], dp_max[2])+c]
    dp_min = [min(dp_min[0], dp_min[1])+a, min(dp_min)+b, min(dp_min[1], dp_min[2])+c]


print(max(dp_max), end=' ')
print(min(dp_min))