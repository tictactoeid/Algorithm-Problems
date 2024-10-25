# Longest Consecutive Sequence
# Medium

class Solution:
    def find(self, num: int) -> int:
        if self.parents[num] == num:
            return num
        parent = self.parents[num]
        self.parents[num] = self.find(parent)
        return self.parents[num]

    def union(self, i: int, j: int) -> int:
        p1 = self.find(i)
        p2 = self.find(j)
        if p1 == p2:
            return
        self.parents[p2] = p1

    def longestConsecutive(self, nums: List[int]) -> int:
        # union find + set
        self.parents = {}
        for num in nums:
            if num in self.parents:
                continue  # duplicate
            self.parents[num] = num
            if num - 1 in self.parents:
                self.union(num - 1, num)
            if num + 1 in self.parents:
                self.union(num, num + 1)

        count = {}
        answer = 0
        for num in self.parents:
            p = self.find(num)
            if p in count:
                count[p] += 1
                answer = max(answer, count[p])
            else:
                count[p] = 1
                answer = max(answer, 1)

        return answer

