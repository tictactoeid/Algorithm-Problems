# Two Sum II - Input Array Is Sorted
# Medium

class Solution:
    # brute force: O(n^2)
    def twoSum_1(self, numbers: List[int], target: int) -> List[int]:
        # Approach 1: Binary Search
        # TC O(nlogn), SC O(1)

        n = len(numbers)
        j = 1
        while j < n:
            i = bisect.bisect_left(numbers[:j], target - numbers[j])
            if i < j and numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            j += 1

    def twoSum(self, numbers, target):
        # Approach 2: Two Pointers
        # TC O(n), SC O(1)
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            value = numbers[i] + numbers[j]
            if value == target:
                return [i + 1, j + 1]
            elif value > target:
                j -= 1
            else:
                i += 1

