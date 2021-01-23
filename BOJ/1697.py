from collections import deque
n, k = map(int, input().split())
q = deque([n])
next_q = deque()
answer = 0
visited = [False] * 100001

while q or next_q:
    if not q:
        q = next_q
        next_q = deque()
        answer += 1
    temp = q.popleft()
    visited[temp] = True
    if temp == k:
        print(answer)
        break
    else:
        arr = [temp + 1, temp - 1, 2 * temp]
        for a in arr:
            if 0 <= a <= 100000:
                if not visited[a]:
                    next_q.append(a)