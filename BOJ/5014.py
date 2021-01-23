from collections import deque
INF = int(1e9)
f, s, g, u, d = map(int, input().split())
distance = [INF] * (f + 1)
distance[s] = 0
q = deque([s])

while True:
    if not q:
        print('use the stairs')
        break
    temp = q.popleft()
    if temp == g:
        print(distance[temp])
        break
    else:
        if 0 < (temp + u) <= f:
            if distance[temp + u] == INF:
                q.append(temp + u)
                distance[temp + u] = distance[temp] + 1
        if 0 < (temp - d) <= f:
            if distance[temp - d] == INF:
                q.append(temp - d)
                distance[temp - d] = distance[temp] + 1
