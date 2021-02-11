from collections import deque

n = int(input())
q = deque([n])
next_q = deque()
answer = 0

while True:
    if not q:
        q = next_q
        next_q = deque()
        answer += 1
    temp = q.popleft()
    if temp == 1:
        print(answer)
        break
    if temp % 3 == 0:
        next_q.append(temp // 3)
    if temp % 2 == 0:
        next_q.append(temp // 2)
    next_q.append(temp - 1)
