# Daily Temperatures
# Medium

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0 for _ in range(n)]
        # monotonic stack
        # 값 대신 index를 저장하여, index와의 위치 차이를 구함

        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)

        return answer


        # 73
        # 76
        # 76 72
        # 76 72 69
        # 76 72 71
        # 76 75