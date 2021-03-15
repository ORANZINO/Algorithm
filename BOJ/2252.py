import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegrees = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1
answer = []
q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    answer.append(now)
    for i in graph[now]:
        indegrees[i] -= 1
        if indegrees[i] == 0:
            q.append(i)
print(*answer)
