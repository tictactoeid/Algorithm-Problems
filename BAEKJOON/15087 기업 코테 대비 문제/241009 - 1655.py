# 가운데를 말해요
# 골드 2

from heapq import *
import sys


class MedianFinder:
    def __init__(self):
        self.minheap = []  # stores large numbers
        self.maxheap = []  # stores small numbers

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        heappush(self.minheap, -heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):  # 같거나 maxheap이 하나 많도록 설정
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        # if len(self.minheap) == len(self.maxheap):
        #     #return (-self.maxheap[0] + self.minheap[0]) / 2
        #     return
        # else:
        return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


finder = MedianFinder()
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    finder.addNum(int(input()))
    print(finder.findMedian())
