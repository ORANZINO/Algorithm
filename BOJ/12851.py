from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
distance = 0
ways = 0
q = deque()
q.append((n, 0))

while q:
    now, dist = q.popleft()
    visited[now] = True
    if now == k:
        if not ways:
            distance = dist
        if dist == distance:
            ways += 1
    if now + 1 <= 100000 and not ways and not visited[now + 1]:
        q.append((now + 1, dist + 1))
    if 0 <= now - 1 and not ways and not visited[now - 1]:
        q.append((now - 1, dist + 1))
    if now * 2 <= 100000 and not ways and not visited[now * 2]:
        q.append((now * 2, dist + 1))

print(distance)
print(ways)
