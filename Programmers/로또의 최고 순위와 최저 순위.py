def solution(lottos, win_nums):
    rank_arr = [6, 6, 5, 4, 3, 2, 1]
    common = len(set(lottos) & set(win_nums))
    worst = rank_arr[common]
    best = rank_arr[common + lottos.count(0)]
    return [best, worst]


"""
최소는 둘 사이의 공통 수가 일치하는 것의 전부일 때,
최대는 0으로 표기된 수들이 모두 일치하는 경우이다.
이를 반영하여 결과를 리턴하면 된다.
"""