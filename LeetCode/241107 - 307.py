# Range Sum Query - Mutable
# Medium

from typing import *

class NumArray:
    def build(self, i, start, end):
        if start == end:
            self.tree[i] = self.nums[start]
        else:
            mid = (start + end) // 2
            # range sum에 대한 segtree이므로, left와 right child의 값을 더한다
            self.tree[i] = self.build(2 * i, start, mid) + self.build(2 * i + 1, mid + 1, end)
        return self.tree[i]

    def query(self, i, start, end, left, right):
        # i, start, end는 segment tree node에 대한 정보 (recursive)
        # left, right는 query하려는 구간 정보
        if left > end or right < start:
            # query 구간이 node 구간을 벗어남
            return 0
        if left <= start and end <= right:
            # node 구간이 query 구간에 완전히 포함됨
            return self.tree[i]
        # 구간이 일부만 겹쳐, child node를 탐색해야 함
        mid = (start + end) // 2
        return self.query(2 * i, start, mid, left, right) + self.query(2 * i + 1, mid + 1, end, left, right)

    def _update(self, i, start, end, idx, value):
        # i, start, end는 segtree의 recursive 접근을 위한 정보
        # idx, value는 nums[idx] = value로 update하겠다는 뜻
        if idx < start or idx > end:
            pass
        elif start == end:
            if start == idx:
                self.tree[i] = value
        else:
            mid = (start + end) // 2
            self.tree[i] = self._update(2 * i, start, mid, idx, value) + self._update(2 * i + 1, mid + 1, end, idx,
                                                                                      value)
        return self.tree[i]

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0 for _ in range(4 * self.n)]
        self.nums = nums
        self.build(1, 0, self.n - 1)

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, 0, self.n - 1, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
obj = NumArray(nums)
print(obj.tree)
obj.update(9, -1)
print(obj.tree)

