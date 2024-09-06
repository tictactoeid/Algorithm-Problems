# 정육점
# 골드 4

# 누적합 ..?

import sys

n, m = map(int, input().split())
meats = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

meats.sort(key=lambda x: (x[1], -x[0])) # 싼 것 우선, 무거운 것 우


last_cost = 0
less_weight_sum = 0  # 현재 고기보다 적은 (즉 무료로 얻을 수 있는) 비용의 고기 무게 합
curr_weight_sum = 0  # 현재 고기와 같은 비용의 고기 무게 합, less_weight_sum 갱신을 위해 기록
curr_cost_sum = 0
tmp = -1

for meat in meats:
    weight = meat[0]
    cost = meat[1]

    if last_cost == cost:
        curr_weight_sum += weight
        curr_cost_sum += cost
        if less_weight_sum + curr_weight_sum >= m:
            if tmp == -1:
                tmp = curr_cost_sum
            else:
                tmp = min(tmp, curr_cost_sum)
            #print(tmp)

    else:
        last_cost = cost
        less_weight_sum += curr_weight_sum

        curr_weight_sum = weight
        curr_cost_sum = cost

        if less_weight_sum + weight >= m:
            if tmp > 0:
                #print('tmp')
                print(min(cost, tmp))
            else:
                #print(f'tmp {tmp} cost {cost}')
                print(cost)
            sys.exit()

print(tmp)
