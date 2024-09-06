# 카드 21
# 실버 4

# list나 Queue로 하면 시간초과 뜨고,
# deque로 해야 통과함.

from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])


def round():
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

while(len(cards) >= 2):
    round()

print(cards.popleft())