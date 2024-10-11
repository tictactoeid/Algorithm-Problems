# IPO
# Hard

import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # capital.sort()
        n = len(capital)
        value = [(capital[i], profits[i]) for i in range(n)]
        value.sort()

        heap = []

        my_cap = w
        idx = 0
        for _ in range(k):
            while idx < n and value[idx][0] <= my_cap:
                heapq.heappush(heap, -value[idx][1])
                idx += 1
            if heap:
                my_cap -= heapq.heappop(heap)

        return my_cap



