# 카드 게임
# 플래티넘 5

import bisect

n, m, k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
input_cards = list(map(int, input().split()))

parents = [i for i in range(n)]


def find(x):
    if parents[x] == x:
        return x
    else:
        parent = parents[x]
        parents[x] = find(parent)
        return parents[x]


def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 == p2:
        return
    parents[p2] = p1


for input_card in input_cards:
    idx = bisect.bisect_right(cards, input_card)
    #print(input_card, cards[idx-1], cards[idx])
    root_idx = find(idx)
    print(cards[root_idx])
    union(root_idx+1, root_idx)
