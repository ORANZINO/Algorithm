def solution(weights, head2head):
    answer = []
    for i, head in enumerate(head2head):
        win, lose = head.count("W"), head.count("L")
        win_rate = win / (win + lose) if (win + lose) > 0 else 0
        heavy_win = 0
        for j in range(len(weights)):
            if weights[j] > weights[i] and head[j] == "W":
                heavy_win += 1
        weight = weights[i]
        answer.append((win_rate, heavy_win, weight, len(weights) - i))
    answer.sort(reverse=True)
    return [len(weights) - a[-1] + 1 for a in answer]


"""
각 정렬요소를 순위대로 튜플에 넣어 리스트로 만들어준 다음에 정렬한다.
이 때, 다른 요소들은 내림차순이지만 복서 번호는 오름차순이므로 복서 번호를 반전해서 튜플에 넣어주는 것을 주의한다.
"""