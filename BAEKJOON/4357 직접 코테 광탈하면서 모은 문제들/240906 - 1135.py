# 뉴스 전하기
# 골드 2

n = int(input())
boss = list(map(int, input().split()))

subordinate = [[] for _ in range(n)]

for i in range(1, n):
    subordinate[boss[i]].append(i)

dp = [0 for _ in range(n)]

for i in range(n-1, -1, -1):
    if not subordinate[i]:
        dp[i] = 0
        continue
    #subordinate[i].sort(reverse=True)

    subordinate_times = [dp[x] for x in subordinate[i]]
    subordinate_times.sort(reverse=True)
    time = 0
    for j in range(len(subordinate_times)):
        time = max(time, subordinate_times[j] + j + 1)
        # 가장 오래 걸리는 부하 + 1분 (1번째로 전화)
        # 그 다음 오래 걸리는 부하 + 2분 (2번째로 전화)
        # ...

    dp[i] = time
# print(boss)
# print(subordinate)
# print(dp)
print(dp[0])
