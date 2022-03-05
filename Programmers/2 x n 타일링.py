def solution(n):
    first, second, answer = 1, 2, None
    if n == 1:
        return first
    elif n == 2:
        return second
    n -= 2
    while n:
        answer = first + second
        first, second = second, answer
        n -= 1
    return answer % 1000000007

