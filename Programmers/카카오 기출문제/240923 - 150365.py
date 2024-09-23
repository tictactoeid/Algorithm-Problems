# 미로 탈출 명령어
# 레벨 3
# 2023 KAKAO BLIND RECRUITMENT


# d l r u 사전순

# 그리디
def solution(n, m, x, y, r, c, k):
    min_dist = k - (abs(x-r) + abs(y-c))
    if min_dist % 2 == 1 or min_dist < 0:
        return "impossible"

    answer = ""
    # d l r u 순이므로, ddddlll... 과 같이 d, l을 최대한 사용한다.

    distance = abs(x - r) + abs(y - c)
    while k > distance:
        if x < n:
            answer += "d"
            x += 1
        elif y > 1:
            answer += "l"
            y -= 1
        elif y < m:
            answer += "r"
            y += 1
        else:
            answer += "u"
            x -= 1
        distance = abs(x - r) + abs(y - c)
        k -= 1

    # d, l 위주로 최대한 이동하다가
    # 남은 거리가 부족해지기 직전 출발점으로 향한다
    # 이때도 d, l, r, u의 우선순위로 움직인다

    if r-x > 0:
        answer += "d" * (r-x)
        if y-c > 0:
            answer += "l" * (y-c)
        else:
            answer += "r" * (c-y)
    else:
        if y-c > 0:
            answer += "l" * (y-c)
        else:
            answer += "r" * (c-y)
        answer += "u" * (x-r)

    return answer
