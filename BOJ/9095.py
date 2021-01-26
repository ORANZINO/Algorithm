from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    q = deque()
    answer = 0
    if 1 <= n:
        q.append(1)
    if 2 <= n:
        q.append(2)
    if 3 <= n:
        q.append(3)
    while q:
        temp = q.popleft()
        if temp == n:
            answer += 1
        if temp + 1 <= n:
            q.append(temp + 1)
        if temp + 2 <= n:
            q.append(temp + 2)
        if temp + 3 <= n:
            q.append(temp + 3)
    print(answer)