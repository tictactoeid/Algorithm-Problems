# K Closest Points to Origin
# Medium

class Solution:
    def kClosest_maxheap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach 1: maxheap
        # O(n logk)
        heap = [(-(x ** 2 + y ** 2), x, y) for x, y in points[:k]]
        heapq.heapify(heap)

        for x, y in points[k:]:
            dist = x ** 2 + y ** 2
            if dist < -heap[0][0]:
                heapq.heappushpop(heap, (-dist, x, y))

        return [[x, y] for _, x, y in heap]

    def kClosest(self, points, k):
        # Approach 2: Binary Search의 응용
        # O(n + n/2 + n/4 + ...) = O(n) (average case)

        distances = [x ** 2 + y ** 2 for x, y in points]
        n = len(points)
        low = min(distances)
        high = max(distances)

        answer = []
        remainder = [i for i in range(n)]

        while k:
            pivot = (low + high) // 2
            closer = []
            farther = []
            for i in remainder:
                if distances[i] <= pivot:
                    closer.append(i)
                else:
                    farther.append(i)

            if len(closer) < k:
                answer += closer
                k -= len(closer)
                remainder = farther
                low = pivot + 1
            elif len(closer) == k:
                answer += closer
                break
            else:
                remainder = closer
                high = pivot - 1

        return [points[i] for i in answer]


