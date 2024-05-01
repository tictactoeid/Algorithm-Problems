# 공주님의 정원
# 골드 3

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


n = int(input())

flowers = [[] for _ in range(n)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    flowers[i] = [(a, b), (c, d)]

flowers.sort(key=lambda x: x[0])




def next_date(month, date):
    if days[month] == date:
        return (month+1, 1)
    else:
        return (month, date+1)


def before_date(month, date):
    if date == 1:
        if month == 1:
            return (0, 0)
        return (month-1, days[month-1])
    return (month, date-1)

count = 0
last = (3, 1)
tmp = [(0, 0), (0, 0)]
greedy = []
for i in range(len(flowers)):
    if last > (11, 30):
        break
    flower = flowers[i]
    tmp_last = tmp[1]
    if flower[0] == flower[1]:
        continue
    if flower[0] <= last:
        # 겹치는 경우
        if flower[1] > tmp_last:
            tmp = flower
    else:
        # 안 겹치는 경우, 즉 시작날짜 갱신
        if i > 0:
            last = tmp_last
            count += 1
            tmp = flower

            # greedy.append(flowers[i-1])
if last != tmp[1] and last <= (11, 30) and tmp[1] > (11, 30) and tmp[0] <= last:
    count += 1
    last = tmp[1]
    # greedy.append(tmp[1])
# print(greedy)

if last <= (11, 30):
    print(0)
else:
    print(count)




