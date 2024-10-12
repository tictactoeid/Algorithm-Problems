# 4Sum II
# Medium

# O(n^2)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        count = 0
        sum1 = {}

        for i in range(n):
            for j in range(n):
                current = nums1[i] + nums2[j]
                if current in sum1:
                    sum1[current] += 1
                else:
                    sum1[current] = 1

        for i in range(n):
            for j in range(n):
                target = -(nums3[i] + nums4[j])

                if target in sum1:
                    count += sum1[target]
                    # nums1, nums2에서 해당 sum 값이 나타난 횟수를 더해야
                    # cartesian product가 됨
        return count
    