# 배열 정렬
# 골드 1
import copy
import heapq

n = int(input())
init_arr = list(map(int, input().split()))
m = int(input())
controls = [tuple(map(int, input().split())) for _ in range(m)]

target = sorted(init_arr)

#visited = set()
distance = {}


q = []
heapq.heappush(q, (0, init_arr))
distance[tuple(init_arr)] = 0

while q:
    dist, arr = heapq.heappop(q)
    if tuple(arr) in distance.keys() and dist > distance[tuple(arr)]:
        continue

    for control in controls:
        l, r, c = control
        l -= 1
        r -= 1
        next_arr = copy.copy(arr)
        tmp = next_arr[l]
        next_arr[l] = next_arr[r]
        next_arr[r] = tmp
        #if not visited[next_arr]
        if tuple(next_arr) not in distance.keys() or distance[tuple(next_arr)] > dist + c:
            distance[tuple(next_arr)] = dist + c
            heapq.heappush(q, (dist + c, next_arr))

if tuple(target) in distance.keys():
    print(distance[tuple(target)])
else:
    print(-1)



