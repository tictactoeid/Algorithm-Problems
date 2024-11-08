# Increasing Triplet Subsequence

class Solution:
    def increasingTriplet_1(self, nums: List[int]) -> bool:
        # Approach 1
        # TC, SC: O(n)
        n = len(nums)

        smaller = [False for _ in range(n)]
        # larger = [False for _ in range(n)]

        minimum = math.inf
        maximum = -math.inf

        for i in range(n):
            if minimum < nums[i]:
                smaller[i] = True
            minimum = min(minimum, nums[i])

        for i in range(n - 1, -1, -1):
            if smaller[i] and maximum > nums[i]:
                return True
            maximum = max(maximum, nums[i])

        return False

    def increasingTriplet_2(self, nums: List[int]) -> bool:
        # Approach 2: smaller 배열을 만드는 대신 nums 배열을 수정
        # TC: O(n)
        # SC: O(1)

        n = len(nums)
        minimum = math.inf
        maximum = -math.inf

        for i, num in enumerate(nums):
            if minimum >= num:
                nums[i] = -math.inf  # useless
            minimum = min(minimum, num)

        for i in range(n - 1, -1, -1):
            if nums[i] == -math.inf:
                continue
            if maximum > nums[i]:
                return True
            maximum = max(maximum, nums[i])
        # print(nums)
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        # Approach 3
        # 가장 작은 2개의 원소를 추적
        # TC: O(n), SC: O(1)

        smallest = [math.inf, math.inf]

        for num in nums:
            if num <= smallest[0]:
                smallest[0] = num
            elif num <= smallest[1]:
                smallest[1] = num
            else:
                return True

        return False

