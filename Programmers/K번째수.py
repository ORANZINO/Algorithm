def solution(array, commands):
    answer = []
    for c in commands:
        temp = sorted(array[(c[0]-1):c[1]])
        answer.append(temp[(c[2]-1)])
    return answer

"""
문제에서 요구하는 그대로를 수행하여 푼 문제.
1. Array 슬라이싱
2. 슬라이스된 부분 Sort
3. Sort된 결과물에서 원하는 인덱스 반환
의 과정을 거쳐 정답을 구할 수 있었다.

"""