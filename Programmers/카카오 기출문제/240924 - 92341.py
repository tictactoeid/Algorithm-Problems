# 주차 요금 계산
# 레벨 2
# 2022 KAKAO BLIND RECRUITMENT

import datetime
import math


def calc_price(fees, car_records):
    total_time = 0

    for i in range(0, len(car_records), 2):
        in_record = car_records[i]
        in_time = datetime.datetime.strptime(in_record[0], "%H:%M")

        if i + 1 < len(car_records):
            out_record = car_records[i + 1]
            out_time = datetime.datetime.strptime(out_record[0], "%H:%M")
        else:
            out_time = datetime.datetime.strptime("23:59", "%H:%M")

        delta = int((out_time - in_time).total_seconds() // 60)
        total_time += delta

    if total_time <= fees[0]:
        price = fees[1]
    else:
        price = fees[1]
        remain = total_time - fees[0]
        price += int(math.ceil(remain / fees[2])) * fees[3]

    return price


def solution(fees, records):
    answer = []
    records.sort(key=lambda x: (x.split()[1], x.split()[0], x.split()[2]))

    current_car = None
    car_records = []

    for record in records:
        r = list(record.split())
        if current_car == r[1]:
            car_records.append(r)

        else:
            if car_records:
                price = calc_price(fees, car_records)
                answer.append(price)

            current_car = r[1]
            car_records = [r]

    if car_records:
        price = calc_price(fees, car_records)
        answer.append(price)

    return answer


# solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
