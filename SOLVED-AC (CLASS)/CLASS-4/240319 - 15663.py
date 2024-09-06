# N과 M (9)
# 실버 2

n, m = map(int, input().split())
line = list(map(int, input().split()))
line.sort()
printed = set()
# 기 출력한 문자열을 저장하여 중복체크
def dfs(i, visited):
    visited.append(i)
    if len(visited) == m:
        out = ""
        for j in visited:
            out += str(line[j])
            out += " "
        out.rstrip()
        if out not in printed:
            print(out)
            printed.add(out)
        return

    for next in range(n):
        if next not in visited:
            dfs(next, visited)
            visited.remove(next)




started = set()
for i in range(n):
    if line[i] not in started:
        dfs(i, [])
        started.add(line[i])