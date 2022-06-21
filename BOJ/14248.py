from collections import deque

N = int(input())
bridge = list(map(int, input().split()))
s = int(input()) - 1
visited = [False] * N
visited[s] = True
q = deque([s])

while q:
    now = q.popleft()
    for i in range(-1, 2, 2):
        temp = now + i * bridge[now]
        if 0 <= temp < N and not visited[temp]:
            q.append(temp)
            visited[temp] = True

print(sum(visited))