# 컬러볼
# 골드 2

# 간단 풀이: 그냥 구현 -> 시간초과 예상

# 각 색상별로 정렬하고 누적합 구해야 할 듯

import sys

n = int(sys.stdin.readline())
balls = [[0, 0] for _ in range(n)]
for i in range(n):
    color, size = map(int, input().split())
    balls[i] = [color - 1, size]


def simple():
    for i in range(n):
        color = balls[i][0]
        size = balls[i][1]
        sum = 0
        for j in range(n):
            if balls[j][0] != color and balls[j][1] < size:
                sum += balls[j][1]
        print(sum)

# simple()

group_sum = [[] for _ in range(n)]
total_sum = []

def cumulative_sum():

    sorted_balls = sorted(balls, key=lambda x: x[1])

    before_sum = 0
    before_size = 0

    for ball in sorted_balls:
        color = ball[0]
        size = ball[1]

        # 전체 누적합 계산
        if before_size != size:
            total_sum.append((size+1, before_sum+size)) # (k, s): size가 k 이상인 경우, s만큼 사로잡을 수 있다.
            before_size = size
            before_sum += size
        else:
            total_sum[-1] = (size+1, before_sum+size)
            before_sum += size

        # 현재 색상의 누적합 계산
        if not group_sum[color]:
            group_before_size = 0
            group_before_sum = 0
        else:
            group_before = group_sum[color][-1]
            group_before_size = group_before[0] - 1
            group_before_sum = group_before[1]
        if group_before_size != size:
            group_sum[color].append((size+1, group_before_sum + size))
        else:
            group_sum[color][-1] = ((size+1, group_before_sum + size))


# AS-IS
# 각 그룹별로 iterate하며 합을 따로 구함
# 그리고 마지막에 각 그룹별로 iterate하며 본인 그룹만 빼고 누적합들을 더함

# TO-BE
# 전체 공을 크기별로 sort함
# 그리고 하나의 큰 배열을 iterate하며 전체 합을 구함
# 이 과정에서 색상 그룹별 합도 구합
# (전체 누적합 중 가능한 최대) - (본인 그룹 누적합 중 가능한 최대) 를 구해 결과를 도출함.


def result():
    for i in range(n):
        player_color = balls[i][0]
        player_size = balls[i][1]
        player_sum = 0

        for j in range(len(total_sum)-1, -1, -1): # 이분 탐색으로 바꾸면 더 빠를듯?
            curr_min_size = total_sum[j][0]
            if player_size >= curr_min_size:
                player_sum = total_sum[j][1]
                break

        group = group_sum[player_color]
        for j in range(len(group)-1, -1, -1):
            curr_tuple = group[j]
            curr_min_size = curr_tuple[0]

            if player_size >= curr_min_size:
                player_sum -= curr_tuple[1]
                break

        print(player_sum)
cumulative_sum()
result()
