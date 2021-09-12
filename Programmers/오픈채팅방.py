def solution(record):
    dic = dict()
    answer = []
    for r in record:
        action = r.split()[0]
        if action != 'Leave':
            _, user_id, name = r.split()
            dic[user_id] = name
            if action == 'Enter':
                answer.append((action, user_id))
        else:
            _, user_id = r.split()
            answer.append((action, user_id))
    for i, a in enumerate(answer):
        if a[0] == 'Enter':
            answer[i] = f'{dic[a[1]]}님이 들어왔습니다.'
        else:
            answer[i] = f'{dic[a[1]]}님이 나갔습니다.'
    return answer


"""
모든 record를 프로세싱하고 최종적인 user_id와 name의 매칭을
반영하여 출력해주는 문제이다.
"""