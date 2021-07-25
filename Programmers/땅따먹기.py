def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

"""
Dynamic Programming으로 2번째 행부터 각 열마다 가장 큰 합의 경우를 메모이제이션한다.
마지막 행에서 가장 큰 경우를 리턴한다.
"""