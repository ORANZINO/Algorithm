import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
steps = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (1, -1), (-1, 1), (0, -1)]
distance = [[INF] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q = deque()
            q.append((i, j, 1))
            distance[i][j] = 0
            while q:
                x, y, dist = q.popleft()
                for step in steps:
                    next_x, next_y = x + step[0], y + step[1]
                    if 0 <= next_x < n and 0 <= next_y < m and distance[next_x][next_y] > dist and arr[next_x][next_y] == 0:
                        distance[next_x][next_y] = dist
                        q.append((next_x, next_y, dist + 1))

print(max(max(d) for d in distance))
