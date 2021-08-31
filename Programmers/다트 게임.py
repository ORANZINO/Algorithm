def check(s):
    if ord('0') <= ord(s) <= ord('9'):
        return 'num'
    elif s == '*' or s == '#':
        return 'op'
    else:
        return 'str'


def solution(dartResult):
    arr = []
    i = 0
    for _ in range(3):
        start = i
        while check(dartResult[i]) == 'num':
            i += 1
        num = dartResult[start:i]
        bonus = dartResult[i]
        if bonus == 'S':
            num = int(num)
        elif bonus == 'D':
            num = int(num) ** 2
        elif bonus == 'T':
            num = int(num) ** 3

        op = None
        i += 1
        if i < len(dartResult) and check(dartResult[i]) == 'op':
            op = dartResult[i]
            i += 1
        if op == '*':
            if arr:
                arr[-1] *= 2
            num *= 2
        elif op == '#':
            num *= -1
        arr.append(num)

    return sum(arr)

