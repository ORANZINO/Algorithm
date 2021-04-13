import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
arr = [input() for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
q = deque()
q.append((x1 - 1, y1 - 1))
distance[x1 - 1][y1 - 1] = 0
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    x, y = q.popleft()
    for step in steps:
        for i in range(1, k + 1):
            next_x, next_y = x + (i * step[0]), y + (i * step[1])
            if next_x == (x2 - 1) and next_y == (y2 - 1):
                print(distance[x][y] + 1)
                exit()
            if 0 <= next_x < n and 0 <= next_y < m and arr[next_x][next_y] == '.':
                if distance[next_x][next_y] == -1:
                    distance[next_x][next_y] = distance[x][y] + 1
                    q.append((next_x, next_y))
                elif (distance[x][y] + 1) > distance[next_x][next_y]:
                    break
            else:
                break
print(-1)
