# 로봇 청소기
# 골드 5

n, m = map(int, input().split())
r, c, d = map(int, input().split())
state = [[] for _ in range(n)]
for i in range(n):
    state[i] = list(map(int, input().split()))


count = 0
while True:
    if state[r][c] == 0:
        state[r][c] = -1
        count += 1
        continue
    elif not (r-1 >= 0 and state[r-1][c] == 0) and not (r < n and state[r+1][c] == 0) and not (c-1 >= 0 and state[r][c-1] == 0) and not (c+1 < m and state[r][c+1] == 0):
        if d == 0:
            if r+1 >= n or state[r+1][c] == 1:
                break
            else:
                r = r+1
                continue
        if d == 1:
            if c-1 < 0 or state[r][c-1] == 1:
                break
            else:
                c = c-1
                continue
        if d == 2:
            if r - 1 < 0 or state[r-1][c] == 1:
                break
            else:
                r = r-1
                continue
        else:
            if c + 1 > m or state[r][c+1] == 1:
                break
            else:
                c = c+1
                continue

    else:
        if d == 0: # 북
            d = 3
            if c-1 >= 0 and state[r][c-1] == 0:
                c = c-1
                continue
        elif d == 1: # 동
            d = 0
            if r-1 >= 0 and state[r-1][c] == 0:
                r = r-1
                continue
        elif d == 2: # 남
            d = 1
            if c+1 <= m-1 and state[r][c+1] == 0:
                c = c+1
                continue
        else: # 서
            d = 2
            if r+1 <= n-1 and state[r+1][c] == 0:
                r = r+1
                continue

print(count)
#print(state)