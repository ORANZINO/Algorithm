def solution(N, stages):
    answer = []
    for i in range(1, N + 1):
        arrive_count = len([stage for stage in stages if stage >= i])
        fail_rate = stages.count(i) / arrive_count if arrive_count > 0 else 0
        answer.append((-fail_rate, i))
    answer.sort()
    return [a[1] for a in answer]


"""
각 스테이지와 그에 따른 실패율을 튜플로 묶어 나열하면 되는 문제.
다만, 실패율은 내림차순으로, 2순위인 단계수는 오름차순으로 나열해야한다는 충돌이 있었다.
이 때문에 실패율을 음수로 변환하여 오름차순으로 정렬하면 올바른 순서를 얻을 수 있도록 하였다.
"""