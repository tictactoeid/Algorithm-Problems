# 피로도
# 레벨 2
# 완전탐색

from itertools import permutations


def solution(k, dungeons):
    answer = -1
    permu = permutations(dungeons)

    for order in permu:
        count = 0
        piro = k
        for dungeon in order:
            if piro >= dungeon[0]:
                piro -= dungeon[1]
                count += 1
        answer = max(answer, count)
        if answer == len(dungeons):
            return answer

    return answer