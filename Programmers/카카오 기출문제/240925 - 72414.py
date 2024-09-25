# 광고 삽입
# 레벨 3
# 2021 KAKAO BLIND RECRUITMENT


# 투 포인터 (슬라이딩 윈도우)로 해결
# log로부터 viewer 기록 시 일일이 더하는 대신 부분합 사용하여 통과


def time_to_index(time_string):
    hours, minutes, seconds = map(int, time_string.split(":"))

    return hours * 3600 + minutes * 60 + seconds


def index_to_time(index):
    seconds = index
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return f"{hours:02}:{minutes:02}:{remaining_seconds:02}"


def solution(play_time, adv_time, logs):
    # if play_time == adv_time:
    #     return adv_time

    viewers = [0 for _ in range(time_to_index(play_time) + 1)]

    for log in logs:
        start, end = log.split("-")
        start = time_to_index(start)
        end = time_to_index(end)
        viewers[start] += 1
        viewers[end] -= 1

        # for i in range(start, end+1):
        #     viewers[i] += 1
    for i in range(len(viewers)-1):
        viewers[i+1] += viewers[i]

    answer = 0
    maximum = 0

    start = 0
    end = start + time_to_index(adv_time)
    current_sum = sum(viewers[start:end])

    while end < len(viewers):
        if current_sum > maximum:
            maximum = current_sum
            answer = start
        elif current_sum == maximum:
            answer = min(answer, start)

        current_sum -= viewers[start]
        current_sum += viewers[end]
        start += 1
        end += 1

    return index_to_time(answer)
