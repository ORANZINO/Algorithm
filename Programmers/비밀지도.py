def process(n, x):
    return '0' * (n - len(x[2:])) + x[2:]


def solution(n, arr1, arr2):
    answer = [[' '] * n for _ in range(n)]
    for i, a in enumerate(arr1):
        temp = process(n, bin(a))
        for j in range(n):
            if temp[j] == "1":
                answer[i][j] = "#"

    for i, a in enumerate(arr2):
        temp = process(n, bin(a))
        for j in range(n):
            if temp[j] == "1":
                answer[i][j] = "#"

    return [''.join(a) for a in answer]


"""
2진수를 표현하고 그에 맞게 #를 채워넣으면 된다.
"""