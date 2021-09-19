def letter_grade(x):
    if x >= 90:
        return "A"
    elif x > 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 50:
        return "D"
    else:
        return "F"


def solution(scores):
    scores = [[scores[j][i] for j in range(len(scores))] for i in range(len(scores))]
    for i in range(len(scores)):
        if (scores[i][i] == max(scores[i]) or scores[i][i] == min(scores[i])) and scores[i].count(scores[i][i]) == 1:
            scores[i].pop(i)
    answer = [sum(score) / len(score) for score in scores]
    return ''.join(letter_grade(a) for a in answer)


"""
개인별로 평가받은 점수를 더 잘 다룰 수 있도록 transpose해준다.
조건대로 자신의 점수가 유일한 최저점 또는 최고점일 때, 제외하도록 해준다.
평균을 구하고, 그에 따른 점수들을 모아 String으로 리턴해주면 완료!
"""