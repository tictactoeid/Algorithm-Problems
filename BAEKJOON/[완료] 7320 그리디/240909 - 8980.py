# 택배
# 골드 1

import sys

n, c = map(int, input().split())
m = int(input())

boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


def subtask_1():
    count = 0
    for box in boxes:
        count += box[2]
    print(min(c, count))


def subtask_2():
    arrive_n_1 = 0
    arrive_n = 0
    start_n_1 = 0
    for box in boxes:
        if box[1] == n - 1:
            arrive_n_1 += box[2]
        elif box[0] != n - 1:  # n-1에서 출발하는 것은 제외: n-1에서는 한 번 비울 것이므로
            arrive_n += box[2]

        if box[0] == n - 1:
            start_n_1 += box[2]

    box_in_truck = 0
    total = 0

    box_in_truck += min(c - box_in_truck, arrive_n_1)  # n-1로 가는 박스를 최대한 먼저 채우고
    box_in_truck += min(c - box_in_truck, arrive_n)  # 남은 공간에 n으로 가는 박스를 최대한 채운다.

    # n-1에 도착
    total += min(c, arrive_n_1)  # 최대한 채웠던 박스를 일단 내린다.
    box_in_truck -= min(c, arrive_n_1)
    box_in_truck += min(c - box_in_truck, start_n_1)  # 남은 공간에 n으로 가는 박스를 최대한 채운다.

    # n에 도착
    total += box_in_truck
    box_in_truck = 0

    print(total)


def subtask_3(boxes):  # subtask 4의 일부 테케 틀림
    # truck의 정보
    # 도착지 별 박스 개수
    # 총 박스 개수
    box_in_truck = [0 for _ in range(n+1)]  # box_in_truck[i]: i번 마을로 가는, 트럭에 실려있는 박스 개수
    total = 0  # 총 배달한 박스 수, 즉 retval
    total_in_truck = 0  # 현재 트럭에 실려있는 총 박스 수, 즉 sum(box_in_truck)

    boxes.sort(key=lambda x: (x[1], x[0]))
    #print(boxes)
    start_box = 0
    for i in range(1, n+1):  # i번 마을에 도착했을 때
        # 내리는 단계
        total += box_in_truck[i]
        total_in_truck -= box_in_truck[i]
        box_in_truck[i] = 0
        remain = c - total_in_truck  # 남은 용량

        #print(box_in_truck)

        # 싣는 단계
        if remain:
            for j in range(start_box, len(boxes)):
                box = boxes[j]
                if box[0] < i:
                    continue
                if box[2] == 0:
                    continue
                arrive = box[1]
                amount = min(remain, box[2])
                total_in_truck += amount
                box_in_truck[arrive] += amount
                boxes[j][2] -= amount
                remain = c - total_in_truck
                if not remain:
                    #start_box = j
                    break
        #print(box_in_truck)
    print(total)

# 골드 1의 벽은 높다..


def subtask_4(boxes):
    boxes.sort(key=lambda x: (x[1], x[0]))
    total = 0
    arr = [c for _ in range(n+1)]
    # arr[i]: i번째 마을에서 트럭 용량
    # 마을을 직접 iterate할 필요가 없음. 각 마을의 트럭 상태만을 가지고 있으면 됨.
    for start, end, weight in boxes:
        amount = min(weight, min(arr[start:end]))
        # start ~ end-1 까지 택배를 들고 있어야 하므로, 해당 구간의 트럭 용량 중 min 값과 비교
        if amount:
            for i in range(start, end):
                arr[i] -= amount
            total += amount
    print(total)

subtask_4(boxes)
