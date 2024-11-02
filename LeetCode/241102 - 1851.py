# Minimum Interval to Include Each Query
# Hard

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # O(nlogn + mlogm)

        queries = sorted([[query, idx] for idx, query in enumerate(queries)])  # O(nlogn)
        intervals.sort()  # O(mlogm)

        idx = 0
        heap = []
        answer = [0 for _ in range(len(queries))]

        # loop의 복잡도는 O(m + nlogn)
        for query, i in queries:
            # O(nlogn) total: heap의 원소는 최대 n개이고 각 원소는 많아야 1번씩만 제거됨
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # n = len(intervals)라고 하면 아래 loop는 O(nlogn)
            # 왜냐하면 outer for loop과 무관하게 inner while loop에서 모든 interval은 1번씩만 compute: O(n)
            # heappush 연산은 O(logk), k = len(heap), k <= n이므로 최악의 경우 O(logn)
            # total O(nlogn)
            while idx < len(intervals) and intervals[idx][0] <= query:
                start, end = intervals[idx]
                if end < query:
                    idx += 1
                    continue
                heapq.heappush(heap, (end - start + 1, end))
                idx += 1

            answer[i] = heap[0][0] if heap else -1

        return answer
