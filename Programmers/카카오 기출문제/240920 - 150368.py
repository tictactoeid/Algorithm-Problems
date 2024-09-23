# 이모티콘 할인행사
# 레벨 2
# 2023 KAKAO BLIND RECRUITMENT

from itertools import product


# 완전 탐색
def solution(users, emoticons):
    answer = [0, 0]

    discounts = product([10, 20, 30, 40], repeat=len(emoticons))
    for discount in discounts:
        prices = [0 for _ in range(len(emoticons))]
        emoticon_plus = 0
        total_bought = 0
        for i in range(len(emoticons)):
            prices[i] = int(emoticons[i] * (100 - discount[i]) / 100)

        for user in users:
            bought = 0
            for i in range(len(emoticons)):
                if discount[i] >= user[0]:
                    bought += prices[i]
            if bought >= user[1]:
                bought = 0
                emoticon_plus += 1
            total_bought += bought

        if answer[0] < emoticon_plus or (answer[0] == emoticon_plus and answer[1] < total_bought):
            answer = [emoticon_plus, total_bought]

    return answer


print(solution([[40, 10000], [25, 10000]], 	[7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]] ,	[1300, 1500, 1600, 4900]))