from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = []
q = deque()
next_q = deque()

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

answer = 0
while q or next_q:
    if not q:
        q = next_q
        next_q = deque()
        answer += 1
    i, j = q.popleft()
    for step in steps:
        x = i + step[0]
        y = j + step[1]
        if (0 <= x < n) and (0 <= y < m):
            if arr[x][y] == 0:
                arr[x][y] = 1
                next_q.append((x, y))
flag = True

for t in arr:
    if 0 in t:
        flag = False
        break
if flag:
    print(answer)
else:
    print(-1)