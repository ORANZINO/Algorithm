from collections import defaultdict
from math import prod


def solution(clothes):
    d = defaultdict(int)
    for cloth in clothes:
        d[cloth[1]] += 1
    arr = d.values()
    answer = prod(i + 1 for i in arr) - 1
    return answer



"""
defaultdict를 사용해 각 부위의 의류마다 카운트해준다.
안 입는 경우를 포함해 모든 원소에 1을 더해 모두 곱해주고 1을 빼주면 시간 초과를 벗어나서 결과를 낼 수 있다. 
"""