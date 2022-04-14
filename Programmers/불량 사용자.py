import re
from collections import defaultdict

def solution(user_id, banned_id):
    def backtrack(idx, result):
        nonlocal dic
        nonlocal user_idx
        if idx == len(banned_id):
            answer.add(''.join(result))
            return
        for user in dic[banned_id[idx]]:
            if result[user] == '0':
                result[user] = '1'
                backtrack(idx + 1, result)
                result[user] = '0'

    dic = defaultdict(list)
    user_idx = {user: i for i, user in enumerate(user_id)}
    answer = set()
    for b in set(banned_id):
        pattern = re.compile('^' + b.replace('*', '\w') + '$')
        for u in user_id:
            if pattern.match(u):
                dic[b].append(user_idx[u])
    backtrack(0, ['0'] * len(user_id))
    return len(answer)

