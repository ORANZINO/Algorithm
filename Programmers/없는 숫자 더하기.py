def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer


"""
1~9 중에 없는 숫자들을 찾고 더해서 리턴하는 걸 구현하기만 하면 되는 문제
"""