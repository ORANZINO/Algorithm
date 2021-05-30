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
