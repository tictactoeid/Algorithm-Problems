# List of Unique Numbers
# 골드 4

# 투 포인터

n = int(input())
sequence = list(map(int, input().split()))

start = 0
end = 0
result = 0

duplicates = set()
count = [0 for _ in range(100001)]

count[sequence[start]] = 1

while True:
    if not duplicates:
        result += (end - start + 1)

        if end < n-1:
            end += 1
            count[sequence[end]] += 1
            if count[sequence[end]] > 1:
                duplicates.add(sequence[end])
        else:
            break

    else:
        count[sequence[start]] -= 1
        if count[sequence[start]] <= 1 and sequence[start] in duplicates:
            duplicates.remove(sequence[start])
        start += 1
        if start > end:
            break

print(result)
