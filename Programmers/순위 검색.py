from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(information, query):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        num = int(info.pop())
        for i in range(5):
            for c in combinations([0, 1, 2, 3], i):
                temp = info.copy()
                for j in c:
                    temp[j] = '-'
                dic[''.join(temp)].append(num)
    for key in dic:
        dic[key].sort()
    for q in query:
        q = q.split(" and ")
        last = q.pop().split()
        q.append(last[0])
        score = int(last[1])
        temp = dic[''.join(q)]
        answer.append(len(temp) - bisect_left(temp, score))

    return answer

