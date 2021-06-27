def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for k in range(len(arr2[0])):
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                answer[i][k] += (arr1[i][j] * arr2[j][k])
    return answer

"""
기본적인 행렬곱셈문제.
for문의 중첩으로 간단하게 풀 수 있다.
파이썬으로도 Multithreading을 사용해서 속도를 올릴 수 있으려나? 
"""