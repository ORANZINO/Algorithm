from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n - k)
else:
    q = deque([n])
    visited = [False] * 100010
    next_q = deque()
    answer = 0
    flag = True
    while flag:
        if not q:
            q = next_q
            next_q = deque()
            answer += 1
        temp = q.popleft()
        visited[temp] = True
        if 0 <= temp * 2 < 100010 and k > temp:
            if temp * 2 == k:
                print(answer)
                break
            if not visited[temp * 2]:
                q.append(temp * 2)
        for i in range(2):
            nxt = temp + (-1) ** i
            if nxt == k:
                print(answer + 1)
                flag = False
                break
            if 0 <= nxt < 100010:
                if not visited[nxt]:
                    next_q.append(nxt)
