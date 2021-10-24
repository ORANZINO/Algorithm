def solution(dirs):
    now = [0, 0]
    dir_dic = {"U": (0, 1), "L": (-1, 0), "R": (1, 0), "D": (0, -1)}
    answer = set()
    for d in dirs:
        next_ = [now[0] + dir_dic[d][0], now[1] + dir_dic[d][1]]
        if all(-5 <= n <= 5 for n in next_):
            answer.add((now[0], now[1], next_[0], next_[1]))
            answer.add((next_[0], next_[1], now[0], now[1]))
            now = next_
    return len(answer) // 2


"""
길을 어떻게 표현할지 고민하다가 애먹었던 문제.
tuple이 set의 member가 될 수 있단 걸 안 후로 고민 끝!
다만 역방향의 경로도 집어넣어 중복 카운트를 막는 것을 잊지 말아야 한다.
"""