# 가장 큰 수
# 레벨 2
# 정렬


def solution(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True, key=lambda x: x*3)
    # 30 vs 3 을 사전 역순으로 정렬 -> 303030 vs 333 을 정렬
    # 모든 string이 len 3 이상이 되도록 함
    answer = ''.join(numbers).lstrip('0')
    if not answer:
        return '0'
    return answer


