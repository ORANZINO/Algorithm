from typing import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        graph = [[] for _ in range(n + 1)]
        distance = [INF] * (n + 1)

        for u, v, w in times:
            graph[u].append((v, w,))

        q = [(0, k,)]
        distance[k] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0],))

        return -1 if INF in distance[1:] else max(distance[1:])

