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


"""
다익스트라 알고리즘을 활용하여 K 이내의 거리에 있는 경로들을 모두 검사한다.
Priority Queue를 이용하여 가장 가까운 거리에 있는 경로부터 검사하고, 그 경로가 dst에 닿는 것일 경우 함수를 종료한다.
그러나, 이렇게 할 경우 dst가 K 안에 없을 때 연산을 낭비하게 되어 시간초과가 발생하므로 그 이전에 BFS를 이용하여
K 거리 안에 dst가 있는지 검증하는 방법을 사용하였다.
"""