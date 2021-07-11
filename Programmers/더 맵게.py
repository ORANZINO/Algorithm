import heapq


def solution(scoville, K):
    count = 0
    scoville.sort()
    while len(scoville) != 1:
        temp = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, temp)
        count += 1
        if scoville[0] >= K:
            return count
    return -1

"""
sort한 후 heap을 사용하여 최소 scoville 지수가 K 이상이 될 때까지 섞는다.
K 이상을 도달했을 경우 섞은 횟수를, 그렇지 않다면 -1을 리턴한다.
"""