import sys
from collections import deque

# count = -1
#
# def dfs(v):
#     count += 1
#     visited[v] = True
#     for e in adj[v]:
#         if not (visited[e]):
#             dfs(e)
#
#
# def bfs(v):
#     q = deque([v])
#     count = -1
#     while q:
#         v = q.popleft()
#         count += 1
#         if not (visited[v]):
#             visited[v] = True
#             for e in adj[v]:
#                 if not visited[e]:
#                     q.append(e)
#     print(count)


n = map(int, sys.stdin.readline())
e = map(int, sys.stdin.readline())
adj = [[] for _ in range(n + 1)]

for _ in range(e):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [False] * (n + 1)

q = deque([1])
count = -1
while q:
    v = q.popleft()
    count += 1
    if not (visited[v]):
        visited[v] = True
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
print(count)