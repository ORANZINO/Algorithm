from collections import defaultdict


def solution(table, languages, preference):
    prefer_dic = defaultdict(int)
    now = 0
    answer = ''
    for i in range(len(languages)):
        prefer_dic[languages[i]] = preference[i]
    for t in table:
        a, *b = t.split()
        temp = sum((len(b) - i) * prefer_dic[b[i]] for i in range(len(b)))
        if temp == now and a < answer:
            answer = a
        elif temp > now:
            now = temp
            answer = a

    return answer



"""
직군별로 언어의 순위에 따른 점수와 선호도 점수를 곱하여 그 합을 비교하는 방식.
같을 때는 직군의 알파벳 순서에 맞춰 출력하도록 처리해주었다.
"""