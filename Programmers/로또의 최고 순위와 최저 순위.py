def solution(lottos, win_nums):
    rank_arr = [6, 6, 5, 4, 3, 2, 1]
    common = len(set(lottos) & set(win_nums))
    worst = rank_arr[common]
    best = rank_arr[common + lottos.count(0)]
    return [best, worst]

