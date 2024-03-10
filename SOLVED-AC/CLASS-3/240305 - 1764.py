# 듣보잡
# 실버 4

n, m = map(int, input().split())
people = set()

result = list()

for _ in range(n):
    name = input()
    people.add(name)

for _ in range(m):
    name = input()
    if name in people:
        result.append(name)

result.sort()
print(len(result))
for person in result:
    print(person)
