def solution(answers):
    answer = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    for idx, a in enumerate(answers):
        a1 = one[idx % 5]
        a2 = two[idx % 8]
        a3 = three[idx % 10]
        if a1 == a:
            answer[0] += 1
        if a2 == a:
            answer[1] += 1
        if a3 == a:
            answer[2] += 1
    for idx, a in enumerate(answer):
        if a == max(answer):
            result.append(idx + 1)
    return result

"""
1, 2, 3번 수포자의 패턴을 리스트로 담아두었다.
answer을 하나씩 검사하며 각 수포자의 답과 비교해본다.
마지막에 가장 많이 맞춘 수포자의 인덱스를 반환해준다.
"""