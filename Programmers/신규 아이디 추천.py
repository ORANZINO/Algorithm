import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('\.{2,}', '.', new_id)
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id


"""
정규표현식이 핵심적이었던 문제.
주어진 direction에 맞추어 규칙을 적용하되, 올바르게 정규식을 사용하는 것이 중요했다.
"""