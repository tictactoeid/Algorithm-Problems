# 비밀번호 찾기
# 실버 4

n, m = map(int, input().split())

password = {}

for _ in range(n):
    site, pw = input().split()
    password[site] = pw

for _ in range(m):
    site = input()
    print(password[site])
