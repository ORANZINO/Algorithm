def solution(n):
    temp = 0
    count = 1
    while temp < n:
        temp += 3 ** count
        count += 1
    n -= temp - (3 ** (count - 1)) + 1
    count -= 2
    answer = ''

    for i in range(count, -1, -1):
        q = n // 3 ** i
        answer += str(q)
        n -= q * 3 ** i
    answer = str(int('1' * (count + 1)) + int(answer))
    return answer.replace('3', '4')

"""
0이 없으므로 각 자리마다 3**n 만큼의 수가 가능.
예) 1자리수 -> 3개, 2자리수 -> 9개
각 자리수는 3의 n승을 의미
예) 4 -> 11 (1 * 3 ** 1 + 1 * 3 ** 0)
"""