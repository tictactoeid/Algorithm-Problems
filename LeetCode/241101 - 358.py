# Rearrange String k Distance Apart
# Hard

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counter = Counter(s)

        last_index = {}
        for char in counter:
            last_index[char] = -math.inf

        heap = []

        for char in counter:
            heapq.heappush(heap, (-counter[char], last_index[char], char))

        # heap을 이용하여, frequency가 높은 character부터 greedy하게 사용
        # 같은 frequency라면 마지막으로 등장한 지 오래된 character부터 우선 사용
        # 만약 frequency가 높지만 거리가 아직 k가 안 된 문자가 있다면 recent에 임시 저장

        answer = ""
        idx = 0
        recent = deque()

        while heap:
            count, last, char = heapq.heappop(heap)
            count *= -1
            if (idx - last) >= k:
                answer += char
                count -= 1
                if count > 0:
                    heapq.heappush(heap, (-count, idx, char))
                idx += 1

                while recent and (idx - recent[0][1]) >= k:
                    count, last, char = recent.popleft()
                    heapq.heappush(heap, (-count, last, char))
            else:
                # TODO
                recent.append([count, last, char])

        if recent:
            return ""
        return answer
