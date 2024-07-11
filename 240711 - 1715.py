# 카드 정렬하기
# 골드 4

# 재활훈련 - 우선순위 큐

import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)


def greedy(cards, cnt):
    while len(cards) > 1:
        card = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        cnt += card
        cnt += card2

        heapq.heappush(cards, card + card2)

    return cnt

print(greedy(cards, 0))
