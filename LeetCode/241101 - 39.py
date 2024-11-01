# Combination Sum
# Medium

class Solution:
    def dfs(self, idx, current_sum, combination):
        if current_sum == self.target:
            self.answer.append(list(combination))  # deep copy
            return

        for i in range(idx, len(self.candidates)):
            if current_sum + self.candidates[i] > self.target:
                return
            else:
                combination.append(self.candidates[i])
                self.dfs(i, current_sum + self.candidates[i], combination)
                combination.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = sorted(candidates)
        self.target = target
        self.dfs(0, 0, [])

        return self.answer