# 개인정보 수집 유효기간
# 레벨 1
# 2023 KAKAO BLIND RECRUITMENT


def should_expire(today, period, privacy_date):
    year, month, day = map(int, privacy_date.split('.'))

    day -= 1

    if day == 0:
        month -= 1
        day = 28

    month += period
    while month > 12 or month < 1:
        if month > 12:
            month -= 12
            year += 1
        elif month < 1:
            month = 12
            year -= 1

    expire_date = "%04d.%02d.%02d" % (year, month, day)

    return expire_date < today


def solution(today, terms, privacies):
    answer = []

    terms_dict = {}
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)

    for i in range(len(privacies)):
        privacy = privacies[i]
        privacy_date, term_key = privacy.split()
        period = terms_dict[term_key]
        if should_expire(today, period, privacy_date):
            answer.append(i+1)

    return answer
