# 멀티탭 스케줄링
# 골드 1

# 어차피 k <= 100밖에 안 되므로
# 예를 들어 현재 1, 2, 3이 있으면
# 뒤에껄 전부 보고 가장 늦게 나오는 걸 빼자!

n, k = map(int, input().split())
devices = list(map(int, input().split()))

codes = [0 for _ in range(n)]

count = 0

for i in range(k):
    device = devices[i]
    if device in codes:
        continue
    if 0 in codes:
        idx = codes.index(0)
        codes[idx] = device
    else:
        next_idxs = [-1 for _ in range(n)]
        for j in range(n):
            try:
                idx = devices[i+1:].index(codes[j])
                next_idxs[j] = idx
            except ValueError:
                break
        if -1 in next_idxs:
            codes[next_idxs.index(-1)] = device
            count += 1
        else:
            codes[next_idxs.index(max(next_idxs))] = device
            count += 1

print(count)