# Minimum Replacements to Sort the Array
# Hard

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)

        # Start from the second last element, as the last one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue

            # Count how many elements are made from breaking nums[i].
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            # It requires numElements - 1 replacement operations.
            answer += num_elements - 1

            # Maximize nums[i] after replacement.
            nums[i] = nums[i] // num_elements

        return answer

    def minimumReplacement_try(self, nums: List[int]) -> int:
        # # 할 수 있는 것
        # # 무조건 큰 수를 쪼갤 수밖에 없다.
        # # 중간에 모난 곳 있으면 멈춰서 쪼개야?
        # # 어떻게 쪼개는 게 최적?

        # 3 4 3
        # 3 2 2 3 -> 1 2 2 2 3 (최적)
        # 3 1 3 3 -> 1 2 3 3 3 -> 1 1 1 3 3 3
        # 3 3 1 3 -> 얜 일단 아닐듯

        # 3 5 3
        # 3 2 3 3 -> 1 2 2 3 3

        # 쪼갤 때 규칙

        # x -> a b
        # a <= b
        # a x b
        # a a x-a b 해서, a <= x-a이면 최적

        count = 0
        idx = len(nums) - 2
        bound = nums[-1]
        # # 마지막 index는 최대한 커야 하므로 쪼갤 일이 없음.

        while idx >= 0:
            if nums[idx] > bound:
                # 쪼개야 함
                # remainder, bound, bound, bound, ..., bound

                if idx == 0:
                    b = bound
                    a = nums[idx] - bound
                else:
                    a = nums[idx] // 2
                    b = nums[idx] - a
                    # if nums[idx] % 2 == 1:
                    #     b = a + 1
                    # else:
                    #     b = a
                    if a > bound:
                        b += (a - bound)
                        a = bound

                    if b > bound:
                        # bound = 2, target = 15인 경우와 같은 edge case
                        a, b = b, a

                nums = nums[:idx] + [a, b] + nums[idx + 1:]
                idx += 1
                # 이제 idx는 nums[idx] - bound 를 가리킴
                # a <= b
                # a <= bound
                # a는 최대한 크게
                count += 1
                # print(nums)
                # bound = min(bound, b)


            else:
                bound = min(bound, nums[idx])
                idx -= 1

        return count
