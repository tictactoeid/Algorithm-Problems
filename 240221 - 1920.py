# 수 찾기
# 실버 4

# list에서 binary search를 이용해 풀었더니 시간 초과가 났다
# binary search를 직접 구현하지 말고, set과 in을 이용해 말 그대로 있는지만 검사해 해결

n = int(input())
a = set(map(int, input().split()))

m = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
    if x in a: print(1)
    else: print(0)
