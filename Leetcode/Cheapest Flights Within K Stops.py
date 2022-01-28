from typing import List
import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n

        for u, v, w in flights:
            graph[u].append((v, w))

        q = collections.deque()
        q.append((src, 0))
        visited[src] = True

        while q:
            now, dist = q.popleft()
            if dist <= k:
                for a, b in graph[now]:
                    if not visited[a]:
                        q.append((a, dist + 1))
                        visited[a] = True

        if not visited[dst]:
            return -1

        q = [(0, src, k)]

        while q:
            d, now, k_left = heapq.heappop(q)
            if now == dst:
                return d
            if k_left >= 0:
                for g in graph[now]:
                    dist = d + g[1]
                    heapq.heappush(q, (dist, g[0], k_left - 1))
        return -1