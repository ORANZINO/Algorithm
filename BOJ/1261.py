import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
m, n = map(int, input().split())
maze = []
smashed = [[INF] * m for _ in range(n)]
for _ in range(n):
    maze.append(list(map(int, input().strip())))

q = []
heapq.heappush(q, (0, 0, 0))
smashed[0][0] = 0
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    smash, y, x = heapq.heappop(q)
    if smashed[y][x] < smash:
        continue
    for step in steps:
        n_x, n_y = x + step[0], y + step[1]
        if 0 <= n_x < m and 0 <= n_y < n:
            cost = maze[n_y][n_x] + smash
            if cost < smashed[n_y][n_x]:
                smashed[n_y][n_x] = cost
                heapq.heappush(q, (cost, n_y, n_x))

print(smashed[n - 1][m - 1])
