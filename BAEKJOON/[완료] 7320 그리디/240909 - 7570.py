# 줄 세우기
# 골드 2

# 입력에서 가장 긴 증가하는 부분수열 (LIS)의 길이를 구한다.
# 나머지 어린이들을 재배열하면 된다. 즉, n - len(LIS)가 정답
# 다만, 어린이들은 앞 또는 뒤로만 재배열할 수 있으므로, LIS는 반드시 연속해야 한다.


n = int(input())
children = list(map(int, input().split()))

indices = [0 for _ in range(n+1)]  # indices[0]은 무효
for i in range(n):
    indices[children[i]] = i

max_length = -1
count = 1  # 자기 자신

for i in range(1, n):
    if indices[i] < indices[i+1]:
        # 예를 들어, 1번 어린이가 2번 어린이보다 앞에 있는 경우
        count += 1
        max_length = max(count, max_length)
    else:
        count = 1  # 연속하지 않다면 리셋

if max_length == -1:
    print(0)
else:
    print(n - max_length)
