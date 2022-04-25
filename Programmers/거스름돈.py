def solution(n, money):
    answer = [0] * (n + 1)
    answer[0] = 1

    for m in money:
        for i in range(m, n + 1):
            answer[i] += answer[i - m]

    return answer[n] % 1000000007

