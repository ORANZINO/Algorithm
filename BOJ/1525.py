from collections import deque

s = ''
goal = '123456780'
for _ in range(3):
    s += ''.join(input().split())
visited = {s: True}
adj = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
ans = -1
time = 0
q = deque()
q.append((s, s.index('0')))
next_q = deque()

while q or next_q:
    if not q:
        q = next_q
        time += 1
        next_q = deque()
    now, zero = q.popleft()
    if now == goal:
        ans = time
        break
    for a in adj[zero]:
        new = list(now)
        new[zero], new[a] = new[a], new[zero]
        new = ''.join(new)
        if new not in visited:
            next_q.append((new, a))
            visited[new] = True
print(ans)
