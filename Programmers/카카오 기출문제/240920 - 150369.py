# 택배 배달과 수거하기
# 레벨 2
# 2023 KAKAO BLIND RECRUITMENT


# greedy
def solution(cap, n, deliveries, pickups):

    dist = 0

    truck = 0

    # last = n-1
    deliver_last = n-1
    pickup_last = n-1
    # TODO: deliver_last와 pickup_last 분리해서 시간 초과 해결.

    while not deliveries[deliver_last] and deliver_last >= 0:
        deliver_last -= 1

    while not pickups[pickup_last] and pickup_last >= 0:
        pickup_last -= 1

    while deliver_last >= 0 or pickup_last >= 0:
        # 물류창고
        truck = cap

        # 집
        deliver_target = deliver_last
        dist += (max(deliver_last, pickup_last) + 1) * 2
        while truck and deliver_target >= 0:
            # 먼 집부터 우선해서 배달
            amount = min(truck, deliveries[deliver_target])
            truck -= amount
            deliveries[deliver_target] -= amount
            deliver_target -= 1

        truck = 0  # 남은 배달 총량 < cap인 예외 케이스 핸들
        pickup_target = pickup_last
        # 수거
        while truck < cap and pickup_target >= 0:
            amount = min(cap-truck, pickups[pickup_target])
            truck += amount
            pickups[pickup_target] -= amount
            pickup_target -= 1

        while not deliveries[deliver_last] and deliver_last >= 0:
            deliver_last -= 1

        while not pickups[pickup_last] and pickup_last >= 0:
            pickup_last -= 1


        # print(deliveries)
        # print(pickups)
        # print()
        #print(last)
    return dist

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# print(solution(2,	7, 	[1, 0, 2, 0, 1, 0, 2], 	[0, 2, 0, 1, 0, 2, 0]))
print(solution(10, 100000, [1]*100000, [1] + [0]*99999))