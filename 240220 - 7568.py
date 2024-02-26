# 덩치
# 실버 5

n = int(input())
people = []
for _ in range(n):
    h, w = input().split()
    people.append((int(h), int(w)))

matrix = [[0 for col in range(n)] for row in range(n)]


# matrix[i][j] > 0 if people[i] > people[j]

def compare(man1, man2):
    if ((man1[0] > man2[0]) and (man1[1] > man2[1])):
        return 1
    elif ((man1[0] < man2[0]) and (man1[1] < man2[1])):
        return -1
    return 0


def getOrder(idx):
    count = 0
    for i in range(n):
        if matrix[i][idx] > 0:  # i > idx
            count += 1
    return count + 1


for i in range(n):
    matrix[i][i] = 0
    for j in range(i + 1, n):
        c = compare(people[i], people[j])
        matrix[i][j] = c
        matrix[j][i] = -1 * c

print(getOrder(0), end='')
for i in range(1, n):
    print(' ', end='')
    print(getOrder(i), end='')
