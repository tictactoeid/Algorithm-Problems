# Find Median from Data Stream
# Hard

class MedianFinder:

    def __init__(self):
        # len(minheap) - len(maxheap) <= 1
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            heapq.heappush(self.minheap, num)
        else:
            if self.minheap[0] <= num:
                heapq.heappush(self.minheap, num)
                if len(self.minheap) - len(self.maxheap) > 1:
                    heapq.heappush(
                        self.maxheap,
                        -heapq.heappop(self.minheap)
                    )
            else:
                heapq.heappush(self.maxheap, -num)
                if len(self.minheap) - len(self.maxheap) < 0:
                    heapq.heappush(
                        self.minheap,
                        -heapq.heappop(self.maxheap)
                    )
        # print(self.maxheap, self.minheap)

    def findMedian(self) -> float:
        if (len(self.maxheap) + len(self.minheap)) % 2 == 1:
            return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
