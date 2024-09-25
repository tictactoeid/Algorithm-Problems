# 순위 검색
# 레벨 2
# 2021 KAKAO BLIND RECRUITMENT

from itertools import product

CPP = 0
JAVA = 1
PYTHON = 2

BE = 0
FE = 1

JR = 0
SR = 1

CHICKEN = 0
PIZZA = 1


def parse_info(info):
    tmp = info.split()
    if tmp[0] == "cpp":
        lang = CPP
    elif tmp[0] == "java":
        lang = JAVA
    else:
        lang = PYTHON

    if tmp[1] == "backend":
        position = BE
    else:
        position = FE

    if tmp[2] == "junior":
        experience = JR
    else:
        experience = SR

    if tmp[3] == "chicken":
        food = CHICKEN
    else:
        food = PIZZA

    score = int(tmp[4])

    return lang, position, experience, food, score


def parse_query(query):
    tmp = query.split()
    if tmp[0] == "cpp":
        lang = [CPP]
    elif tmp[0] == "java":
        lang = [JAVA]
    elif tmp[0] == "python":
        lang = [PYTHON]
    else:
        lang = [CPP, JAVA, PYTHON]

    if tmp[2] == "backend":
        position = [BE]
    elif tmp[2] == "frontend":
        position = [FE]
    else:
        position = [BE, FE]

    if tmp[4] == "junior":
        experience = [JR]
    elif tmp[4] == "senior":
        experience = [SR]
    else:
        experience = [JR, SR]

    if tmp[6] == "chicken":
        food = [CHICKEN]
    elif tmp[6] == "pizza":
        food = [PIZZA]
    else:
        food = [CHICKEN, PIZZA]

    score = int(tmp[7])

    return product(lang, position, experience, food), score


def solution(info, query):
    answer = []
    result = [[[[[0 for _ in range(100001)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]

    for person_info in info:
        lang, position, experience, food, score = parse_info(person_info)
        result[lang][position][experience][food][score] += 1

    for lang in range(3):
        for position in range(2):
            for experience in range(2):
                for food in range(2):
                    for i in range(100000, 0, -1):
                        result[lang][position][experience][food][i-1] += result[lang][position][experience][food][i]


    for q in query:
        product, score = parse_query(q)
        tmp = 0
        for lang, position, experience, food in product:
            tmp += result[lang][position][experience][food][score]

        answer.append(tmp)



    print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])

