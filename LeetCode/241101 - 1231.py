# Divide Chocolate
# Hard

class Solution:
    def can_divide(self, min_total_sweet, sweetness, k):
        remain = k + 1

        pos = 0
        current_sweet = 0

        while remain > 0 and pos < len(sweetness):
            current_sweet += sweetness[pos]
            if current_sweet < min_total_sweet:
                pos += 1
                continue
            else:
                pos += 1
                remain -= 1
                current_sweet = 0

        if remain <= 0:
            return True
        else:
            return False

    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # O(log n)

        # total sweetness = x라고 하자
        # 모든 chocolate bar가 x 이상이면서 최소한의 sweetness를 갖도록, 그러면서 조각이 k+1개 이상이 되도록 자른다면
        # 내가 먹을 total sweetness는 x (또는 x보다 살짝 큰 수)가 될 것이다
        # x를 너무 크게 잡으면 조각을 k+1개로 못 나누고 x를 너무 작게 잡으면 gain이 줄어든다.
        # 즉 조건을 만족하는 x의 최댓값을 찾아야 한다. => Binary Search!

        low = 0
        high = 10 ** 9
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if self.can_divide(mid, sweetness, k):
                answer = max(answer, mid)
                low = mid + 1
            else:
                high = mid - 1

        return answer

