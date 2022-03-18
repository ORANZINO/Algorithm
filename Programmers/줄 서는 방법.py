from math import factorial
def solution(n, k):
    source = [i for i in range(1, n + 1)]
    answer = []
    divider = factorial(n - 1)
    for temp in range(n - 1, 0, -1):
        quotient, k, divider = int(k // divider), k % divider, divider // temp
        if k == 0:
            answer.append(source.pop(quotient - 1))
            answer += reversed(source)
            break
        answer.append(source.pop(quotient))
    return answer

