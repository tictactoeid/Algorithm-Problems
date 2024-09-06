# 카드 합체 놀이
# 실버 1

from heapq import *

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapify(cards)

for _ in range(m):
    card1 = heappop(cards)
    card2 = heappop(cards)
    heappush(cards, card1 + card2)
    heappush(cards, card1 + card2)

print(sum(cards))
