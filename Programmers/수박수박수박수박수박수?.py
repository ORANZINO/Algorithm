def solution(n):
    return '수박' * (n // 2) + '수' * (n % 2)


"""
n이 짝수라면 '수박'을 n // 2 번 반복해주면 되고
홀수라면 n // 2 번 반복해준 후에 '수'를 한 번 더 붙여주면 된다.
"""