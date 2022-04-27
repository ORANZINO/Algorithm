import heapq


def solution(n, works):
    new_works = []

    for work in works:
        heapq.heappush(new_works, -work)

    while n:
        now = heapq.heappop(new_works)
        if now == 0:
            break
        now += 1
        n -= 1
        heapq.heappush(new_works, now)

    return sum(w ** 2 for w in new_works)

