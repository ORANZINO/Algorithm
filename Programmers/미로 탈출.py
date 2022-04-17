import heapq
from collections import defaultdict


def solution(n, start, end, roads, traps):
    INF = int(1e9)
    distance = [defaultdict(lambda: INF) for _ in range(n + 1)]
    distance[start][0] = 0
    graph = [[[] for _ in range(n + 1)] for _ in range(2)]
    for p, q, s in roads:
        graph[0][p].append((q, s))
        graph[1][q].append((p, s))
    q = [(0, start, 0)]
    trap = 0
    for t in traps:
        trap |= 1 << t

    while q:
        d, now, trapped = heapq.heappop(q)
        if now == end:
            return d
        if (1 << now) & trap:
            trapped ^= 1 << now
        for dest, dist in graph[bool((1 << now) & trapped)][now]:
            if not (trapped & (1 << dest)) and (d + dist) < distance[dest][trapped]:
                distance[dest][trapped] = d + dist
                heapq.heappush(q, (d + dist, dest, trapped))
        for dest, dist in graph[not bool((1 << now) & trapped)][now]:
            if (trapped & (1 << dest)) and (d + dist) < distance[dest][trapped]:
                distance[dest][trapped] = d + dist
                heapq.heappush(q, (d + dist, dest, trapped))

    return 0

