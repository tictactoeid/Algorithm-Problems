# Partition Equal Subset Sum
# Medium

# Knapsack

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2

        # 각 element 입장에서 보면
        # 넣느냐, 안 넣느냐 2가지 방법이 존재

        # dp[i][s] => i번째 element까지 고려, 선택한 원소들의 합이 s

        # i번째를 선택하는 경우

        # dp[i][s] = dp[i-1][s-nums[i]]

        # 아닌 경우
        # dp[i][s] = dp[i-1][s]
        # 참고로 가능/불가능 여부만 기록하면됨

        # dp = n * target 배열
        # -> 공간 복잡도가 너무 커지므로

        # dp = n개의 set?

        dp = [set() for _ in range(n)]

        dp[0].add(0)
        dp[0].add(nums[0])

        for i in range(1, n):
            for x in dp[i - 1]:
                if x + nums[i] == target or x == target:
                    return True
                dp[i].add(x)
                dp[i].add(x + nums[i])

        return False