# 회의실 배정
# 실버 1

# 그리디?

n = int(input())

time = []
last_end = 0
count = 0

for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: (x[1], x[0]))

for i in time:
    start = i[0]
    end = i[1]
    if start >= last_end:
        #print(start, end)
        last_end = end
        count += 1

print(count)
