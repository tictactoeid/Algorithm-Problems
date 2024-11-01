# Smallest Range Covering Elements from K Lists
# Hard

class Solution:
    def smallestRange_unoptimized(self, nums: List[List[int]]) -> List[int]:
        # heap에 모든 원소를 때려넣고
        # 하나씩 pop하며 queue에 기록
        # x번 list의 j번 원소가 queue에 들어왔다면, 그 순간 x번 list의 j-1번 이하 원소는 전부 버릴 예정임
        # 이것들이 queue의 맨 앞에 오는 순간 버림
        # 그리고 queue에 모든 list의 원소들이 1번씩 들어왔다는 전제 하에, 항상 queue의 (first, last)를 찍으면 유효한 구간이 됨

        k = len(nums)
        heap = []
        for i in range(k):
            tmp = [(nums[i][j], i, j) for j in range(len(nums[i]))]
            heap += tmp

        heapq.heapify(heap)

        indices = [-1 for _ in range(k)]
        queue = deque()
        flag = False
        answer = [-math.inf, math.inf]


        while heap:
            num, i, j = heapq.heappop(heap)
            indices[i] = j

            while queue and queue[0][2] < indices[queue[0][1]]:
                queue.popleft()
            queue.append((num, i, j))
            #print(num, i, j, queue)
            if flag or -1 not in indices:  # flag 없어도 됨. 그냥 같은 조건을 반복적으로 체크하는 것을 막는 용도
                flag = True
                a, b = queue[0][0], queue[-1][0]
                c, d = answer
                if b - a < d - c or (b-a == d-c and a<c):
                    #print(answer, [a, b])
                    answer = [a, b]

        return answer


    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # optimized
        # idea: 어차피 queue의 max, min만 필요하므로, queue는 사실 필요가 없음
        # 자연스럽게, 처음에 모든 값을 heap에 담을 필요도 없음.
        # heap의 top을 min value로, 마지막으로 heap에 집어넣은 값을 max value로 하면 되고
        # queue에서 쓸모없는 값을 popleft하는 부분은 heap을 pop하며 자연스럽게 구현됨.

        k = len(nums)
        heap = []
        max_value = -math.inf

        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        answer = [-math.inf, math.inf]

        while heap:
            min_value, i, j = heapq.heappop(heap)
            #print(min_value,i,j)

            c, d = answer
            if max_value - min_value < d - c:
                answer = [min_value, max_value]

            if j+1 < len(nums[i]):
                heapq.heappush(heap, (nums[i][j+1], i, j+1))
                max_value = max(max_value, nums[i][j+1])
            else:
                break

        return answer
