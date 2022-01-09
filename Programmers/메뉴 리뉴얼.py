from itertools import combinations
from collections import Counter


def solution(orders, course):
    orders = [list(order) for order in orders]
    result = []
    for c in course:
        counter = Counter(''.join(sorted(com)) for order in orders for com in combinations(order, c)).most_common()
        if counter[0][1] < 2: break
        for item in counter:
            if item[1] == counter[0][1]: result.append(item[0])
            else: break
    return sorted(result)


"""
각 단어들에서 가장 많이 나온 조합들을 센 후에 정렬하여 리턴한다
"""