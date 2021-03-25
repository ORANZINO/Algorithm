import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().strip().split())
    graph[a].append((cost, b))
start, dest = map(int, input().strip().split())
distance = [INF] * (n + 1)
distance[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] >= dist:
        for a, b in graph[now]:
            cost = dist + a
            if distance[b] > cost:
                heapq.heappush(q, (cost, b))
                distance[b] = cost
print(distance[dest])
