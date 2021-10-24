def solution(n):
    for i in range(2, n):
        if (n - 1) % i == 0:
            return i


"""
나머지가 1이 되는 수를 찾고 return해주는 방식
"""