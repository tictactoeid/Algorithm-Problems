# Russian Doll Envelopes
# Hard

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # [1, 1] [2, 5] [3, 4] [4, 5]

        # [1, 1] [2, 5] -> x
        # [1, 1] [3, 4] [4, 5] -> o

        # height로 정렬, height가 같으면 width의 역순으로 정렬
        # 그리고 width로 LIS -> height가 작은 쪽이 더 왼쪽에
        # 예외 케이스는 height가 같지만 width가 더 큰 경우: 이 경우 하나만 넣을 수 있음
        # 이때 width의 역순으로 정렬했으므로 어차피 하나만 선택됨.

        answer = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        for envelop in envelopes:
            idx = bisect.bisect_left(answer, envelop[1])
            if idx >= len(answer):
                answer.append(envelop[1])
            else:
                answer[idx] = envelop[1]

        return len(answer)
