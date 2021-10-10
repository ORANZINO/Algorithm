def solution(s):
    answer = 0
    count = 0
    while s != '1':
        answer += s.count('0')
        s = bin(s.count('1'))[2:]
        count += 1
    return count, answer


"""
1이 될 때까지 주어진 내용대로 계속 이진 변환해주면 된다.
따로 이진수 구하는 함수를 짜기보다는 있는 함수를 썼다.
"""