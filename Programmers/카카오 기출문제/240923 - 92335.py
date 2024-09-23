# k진수에서 소수 개수 구하기
# 레벨 2
# 2022 KAKAO BLIND RECRUITMENT


import math


def convert(n, k):
    result = ""

    exp = math.floor(math.log(n, k))

    while exp >= 0:
        result += str(n // (k ** exp))
        n %= (k ** exp)
        exp -= 1

    return result


# def restore(n, k):
#     result = 0
#     n = n[::-1]
#
#     for i in range(len(n)):
#         result += (k ** i) * int(n[i])
#
#     return result
#


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0 and n // i > 1:
            return False
        i += 1
    return True


def solution(n, k):
    answer = 0

    primes = convert(n, k).split("0")
    #print(primes)
    for prime in primes:
        if not prime:
            continue
        else:
            if is_prime(int(prime)):
                answer += 1


    return answer


# print(restore(convert(437674, 3), 3))
# print(restore("211020101011", 3))

print(solution(437674 	,3))