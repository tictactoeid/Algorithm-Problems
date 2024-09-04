# 베스트앨범
# 레벨 3
# 해시

# "classic": [1450, [0, 2, 3]]
# [0, 2, 3]의 sort key로 plays[i]를 사용

def solution(genres, plays):
    answer = []

    genre_dict = {}
    for i in range(len(genres)):
        key = genres[i]
        if key in genre_dict.keys():
            genre_dict[key][0] += plays[i]
            genre_dict[key][1] += [i]
        else:
            genre_dict[key] = [plays[i], [i]]

    sorted_values = list(genre_dict.values())
    sorted_values.sort(key=lambda x: x[0], reverse=True)
    #print(sorted_values)
    for value in sorted_values:
        tmp = value[1]
        tmp.sort(key=lambda x: plays[x], reverse=True)
        answer += tmp[:2]

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
