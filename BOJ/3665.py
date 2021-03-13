from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    rank = list(map(int, input().split()))
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            graph[rank[j]][rank[i]] = True
            indegree[rank[i]] += 1
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if not graph[a][b]:
            a, b = b, a
        graph[a][b], graph[b][a] = False, True
        indegree[a] += 1
        indegree[b] -= 1
    q = deque()
    answer = []
    count = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            count += 1
            q.append(i)
    if count != 1:
        if count > 1:
            print("?")
        elif count == 0:
            print("IMPOSSIBLE")
        continue
    while q and count == 1:
        count = 0
        now = q.popleft()
        answer.append(now)
        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    count += 1
                    q.append(i)
    if count > 1:
        print("?")
    elif len(answer) != n:
        print("IMPOSSIBLE")
    else:
        print(*answer[::-1])
