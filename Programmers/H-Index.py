def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

"""
정렬한 후에 처음 원소부터 H-Index의 정의조건을 충족하는지 검사합니다.
"""