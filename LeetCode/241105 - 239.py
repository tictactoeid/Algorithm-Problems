# Sliding Window Maximum
# Hard

# Monotonic Queue, O(n).

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)

        answer = [0 for _ in range(n - k + 1)]

        # initialize monotonic queue
        for i in range(k):
            value = nums[i]
            while q and q[-1][0] <= value:
                q.pop()
            q.append((value, i))
        answer[0] = q[0][0]
        # print(q)

        for i in range(k, n):
            value = nums[i]
            while q and q[-1][0] <= value:
                q.pop()
            q.append((value, i))
            while q and q[0][1] <= i - k:  # out of range
                q.popleft()

            answer[i - k + 1] = q[0][0]
            # print(q)

        return answer

