def solution(d, budget):
    d.sort()
    i = 0
    while budget >= 0 and i < len(d):
        budget -= d[i]
        i += 1

    return i if i == len(d) and budget >= 0 else i - 1


"""
주어진 배열을 정렬해서 예산에서 작은 것부터 빼주며 카운트
"""