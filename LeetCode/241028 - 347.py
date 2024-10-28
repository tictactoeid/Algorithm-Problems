# Top K Frequent Elements
# Medium

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        tmp = sorted([(x, freq[x]) for x in freq], key=lambda x: -x[1])
        answer = [x[0] for x in tmp[:k]]
        return answer