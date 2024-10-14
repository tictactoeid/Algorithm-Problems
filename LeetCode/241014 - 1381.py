# Design a Stack With Increment Operation
# Medium

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        value = self.stack.pop(-1)
        return value

    def increment(self, k: int, val: int) -> None:
        n = len(self.stack)
        for idx in range(k):
            if idx > n - 1:
                break
            self.stack[idx] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
