# Max Stack
# Hard

class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set()
        self.idx = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.idx))
        heapq.heappush(self.heap, (-x, -self.idx))
        self.idx += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            del self.stack[-1]

        value, idx = self.stack[-1]
        del self.stack[-1]
        self.removed.add(idx)
        return value

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            del self.stack[-1]

        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)

        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)

        value, idx = heapq.heappop(self.heap)
        self.removed.add(-idx)
        return -value

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()