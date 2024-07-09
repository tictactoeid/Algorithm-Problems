# 컨베이어 벨트 위의 로봇
# 골드 5

n, k = map(int, input().split())
a = list(map(int, input().split()))

zeros = 0
count = 0
up = 0
down = (up + n - 1) % (2*n)
robots = []

while True:
    count += 1

    # 1
    up = (up - 1) % (2*n)
    down = (up + n - 1) % (2*n)

    # 2
    i = 0
    while i < len(robots):
        if robots[i] == down:
            del robots[i]
            continue

        next = (robots[i] + 1) % (2*n)
        if next not in robots and a[next] > 0: # 이동 가능
            a[next] -= 1
            if a[next] == 0:
                zeros += 1
            if next == down: # 이동 후 즉시 내림
                del robots[i]
                continue
            else:
                # a[next] -= 1
                # if a[next] == 0:
                #     zeros += 1
                robots[i] = next # 이동
        i += 1

    # 3
    if a[up] != 0:
        robots.append(up)
        a[up] -= 1
        if a[up] == 0:
            zeros += 1

    # 4
    if zeros >= k:
        break

print(count)


