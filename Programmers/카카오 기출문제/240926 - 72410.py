# 신규 아이디 추천
# 레벨 1
# 2021 KAKAO BLIND RECRUITMENT

import re

def solution(new_id):

    for i in range(len(new_id)):
        if new_id[i].isupper():
            new_id = new_id[:i] + new_id[i].lower() + new_id[i+1:]

    new_id = re.sub(r'[^a-z0-9._-]', '', new_id)
    new_id = re.sub(r'\.\.+', '.', new_id)

    if new_id and new_id[0] == '.':
        new_id = new_id[1:]

    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    if not new_id:
        new_id = 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

print(solution(  	"=.="))