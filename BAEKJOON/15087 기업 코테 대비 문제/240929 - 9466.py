# 텀 프로젝트
# 골드 3

# 시간 초과

t = int(input())
for _ in range(t):
    n = int(input())
    students = list(map(int, input().split()))

    team = [0 for _ in range(n+1)]

    current_team_no = 1
    current_team = []
    cnt = 0

    for i in range(1, n+1):
        if team[i] != 0:
            continue
        next_student = i
        while True:
            current_team.append(next_student)
            next_student = students[next_student-1]
            if team[next_student] != 0:
                for std in current_team:
                    team[std] = -1
                current_team = []
                break

            #if next_student in current_team:
            try:
                idx = current_team.index(next_student)
                for x in current_team:
                    team[x] = -1
                # for std in current_team[idx:]:
                #     team[std] = current_team_no
                #
                # for std in current_team[:idx]:
                #     team[std] = -1
                # current_team_no += 1

                cnt += len(current_team) - idx
                current_team = []
                break
            except ValueError:
                continue

            # if next_student == current_team[0]:
            #     for std in current_team:
            #         team[std] = current_team_no
            #     current_team_no += 1
            #     current_team = []
            #     break
            # elif next_student in current_team:
            #     # idx = current_team.index(next_student)
            #     # for std in current_team[:idx]:
            #     #     team[std] = -1
            #     # current_team = current_team[idx:]
            #     current_team = []
            #     break

    # result = 0
    # for x in range(1, n+1):
    #     if team[x] == 0 or team[x] == -1:
    #         result += 1
    #
    #print(team)
    # print(result)
    print(n-cnt)
