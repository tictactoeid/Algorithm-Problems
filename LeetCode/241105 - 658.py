# Find K Closest Elements
# Medium

class Solution:
    def findClosestElements_heap(self, arr: List[int], k: int, x: int) -> List[int]:
        # Approach 1: use max heap with length <= k
        # O(nlogk), n >= k이므로

        heap = []

        for i in range(len(arr)):  # O(n)
            distance = abs(arr[i] - x)
            value = arr[i]
            if len(heap) < k:
                heapq.heappush(heap, (-distance, -value))
            else:
                heapq.heappushpop(heap, (-distance, -value))  # O(logk)

        answer = sorted([-value for _, value in heap])  # O(klogk)
        return answer

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Approach 2: use binary search to find closest and compare neighborhoods via sliding window
        # O(k + logn)
        n = len(arr)

        idx = bisect.bisect_left(arr, x)  # O(log n)
        left = arr[idx - 1] if idx > 0 else math.inf
        right = arr[idx] if idx < n else math.inf

        if abs(left - x) <= abs(right - x):
            closest = idx - 1
        else:
            closest = idx

        start = max(closest + 1 - k, 0)
        end = start + k - 1

        while end < n - 1 and start <= closest:  # O(k)
            if abs(arr[start] - x) <= abs(arr[end + 1] - x):
                # current is the answer.
                return arr[start:end + 1]

            start += 1
            end += 1

        return arr[-k:]

