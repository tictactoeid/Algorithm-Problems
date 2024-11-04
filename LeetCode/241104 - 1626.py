# Best Team With No Conflicts
# Medium

# 어려운 Medium dp 문제

class Solution:
    def bestTeamScore_first(self, scores: List[int], ages: List[int]) -> int:
        # age = x, score = y인 player를 골랐다면
        # age <= x-1인 선수는 score <= y.

        # dp[i][j]: age 역순으로 정렬하여, i번째 선수까지 고려했을 때 최소 score가 j
        # 이러면 공간복잡도가 1000 * 10^6이니까
        # dp[i][j] : i번째 선수까지 고려했을 때 j번째 선수의 score가 가장 최소로 하자

        # 아직 1명도 안 고른 상태를 추가 고려해야 함
        # age가 같을 때는 무조건 score가 높은 선수부터 고려하므로 나이가 낮은 선수에 대해서만 conflict가 적용된다는 것은 무시해도 됨

        n = len(scores)
        players = [(ages[i], scores[i]) for i in range(n)]
        players.sort(key=lambda x: (-x[0], -x[1]))

        dp = [[0 for _ in range(n)] for _ in range(n)]

        dp[0][0] = players[0][1]  # pick player 0.

        for i in range(1, n):
            current_score = players[i][1]
            dp[i][i] = current_score  # 앞에서 아무도 안 고르고, 현재 선수만 고르는 경우

            for s in range(0, i + 1):
                dp[i][s] = max(dp[i - 1][s], dp[i][s])
                score_bound = players[s][1]
                if current_score > score_bound:
                    # conflict. cannot pick
                    continue
                else:
                    dp[i][i] = max(dp[i][i], dp[i - 1][s] + current_score)

        return max(dp[-1])

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # TC: O(n^2)
        # SC: O(n^2) -> O(n), optimized

        n = len(scores)
        players = [(ages[i], scores[i]) for i in range(n)]
        players.sort(key=lambda x: (-x[0], -x[1]))

        dp = [0 for _ in range(n)]  # 어차피 직전 row만 보기 때문에 1d array로도 가능

        dp[0] = players[0][1]  # pick player 0.

        before_max = dp[0] if n > 1 and players[0][1] >= players[1][1] else -math.inf

        for i in range(1, n):
            current_score = players[i][1]
            dp[i] = max(current_score, before_max + current_score)

            before_max = -math.inf
            for s in range(0, i + 1):
                if s < i:
                    # dp[i][s] = dp[i-1][s]
                    pass
                if i < n - 1 and players[s][1] >= players[i + 1][1]:
                    before_max = max(before_max, dp[s])
        return max(dp)
