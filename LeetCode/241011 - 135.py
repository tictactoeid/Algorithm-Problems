# Candy
# Hard

class Solution:
    def candy_sort(self, ratings: List[int]) -> int:
        # 처음 생각한 풀이
        # rating 순으로 정렬 후, 낮은 rating부터 주변을 채우면
        # 낮은 rating은 나중에 candy가 추가될 일이 없으므로 greedy하게 해결할 수 있다

        n = len(ratings)
        candies = [1 for _ in range(n)]

        sorted_ratings = sorted(list(enumerate(ratings)), key=lambda x: x[1])

        for idx, rating in sorted_ratings:
            if idx > 0 and ratings[idx - 1] > rating and candies[idx - 1] <= candies[idx]:
                candies[idx - 1] = candies[idx] + 1
            if idx < n - 1 and ratings[idx + 1] > rating and candies[idx + 1] <= candies[idx]:
                candies[idx + 1] = candies[idx] + 1

        return sum(candies)

    def candy(self, ratings: List[int]) -> int:
        # 최적 풀이: 정렬 없이 O(n)
        # 먼저 왼쪽 -> 오른쪽으로 iterate하며, 오른쪽이 더 큰 경우에만 채운다
        # 이후 오른쪽 -> 왼쪽으로 iterate하며, 왼쪽이 더 큰 경우에만 채운다

        # iterate에서 이미 지나온 학생은 candy를 주지 않는 것은 동일
        # 좌우 모두 비교하기 위해, 2번 iterate하는 것이 핵심

        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                candies[i + 1] = candies[i] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)
