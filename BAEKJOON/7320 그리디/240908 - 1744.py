# 수 묶기
# 골드 4
# 2트

n = int(input())
sequence = list(int(input()) for _ in range(n))
sequence.sort()
considered = [False for _ in range(n)]  # 중복 처리 로직
result = 0

for i in range(n-1, -1, -1):
    if considered[i] or considered[i-1]:
        continue

    if sequence[i] > 0 and sequence[i-1] > 0:
        if sequence[i] == 1 or sequence[i-1] == 1:
            result += max(sequence[i] + sequence[i-1], sequence[i] * sequence[i-1])
        else:
            result += sequence[i] * sequence[i-1]
        considered[i] = True
        considered[i-1] = True
    elif sequence[i] > 0 and sequence[i-1] <= 0:
        # result += sequence[i]
        # considered[i] = True
        break
    else:  # seq[i] <= 0
        break

for i in range(0, n, 2):
    if considered[i]:
        break
    if i == n-1:
        result += sequence[i]
        break
    if not considered[i+1]:
        if sequence[i] < 0 and sequence[i+1] < 0:
            result += sequence[i] * sequence[i+1]
        elif sequence[i] < 0 and sequence[i+1] == 0:
            result += 0
        else:
            result += max(sequence[i] * sequence[i+1], sequence[i] + sequence[i+1])
    else:
        result += sequence[i]

print(result)


# 틀렸던 이유
# 1. 0 이하 / 0 초과 나눠서 생각하는데, 0 근처 값들의 중복 처리를 실수함
# 2. (1, n)의 경우 묶지 않는 것이 이득인데, (1, 1)만 생각하고 (1, n)을 생각 못 함.
# 해당 테스트 케이스: 3 -1 1 2 -> ans: 2