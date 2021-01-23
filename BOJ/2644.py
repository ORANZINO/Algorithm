from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
a, b = map(int, input().split())
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
q = deque([a])
next_q = deque()

while True:
    if not q:
        if not next_q:
            print(-1)
            break
        else:
            q = next_q
            next_q = deque()
            answer += 1
    else:
        temp = q.popleft()
        visited[temp] = True
        if temp == b:
            print(answer)
            break
        else:
            for t in graph[temp]:
                if not visited[t]:
                    next_q.append(t)