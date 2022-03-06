from collections import defaultdict
import heapq

def solution(genres, plays):
    dic = defaultdict(list)
    for i in range(len(genres)):
        heapq.heappush(dic[genres[i]], (-plays[i], i))
    val = sorted(dic.values(), key=lambda arr: sum(t[0] for t in arr))
    answer = []
    for v in val:
        answer.append(heapq.heappop(v)[1])
        if v:
            answer.append(heapq.heappop(v)[1])
    return answer

