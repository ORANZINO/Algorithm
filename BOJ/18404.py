from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[-1] * (n + 1) for _ in range(n + 1)]
target = [[False] * (n + 1) for _ in range(n + 1)]
ans = []
x, y = list(map(int, input().split()))
for _ in range(m):
    a, b = map(int, input().split())
    ans.append((a, b))
    target[a][b] = True
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
q = deque()
q.append((0, x, y))
arr[x][y] = 0

while m:
    dist, x, y = q.popleft()

    for step in steps:
        nx, ny = x + step[0], y + step[1]
        if 0 < nx <= n and 0 < ny <= n and arr[nx][ny] < 0:
            q.append((dist + 1, nx, ny))
            if target[nx][ny]:
                m -= 1
            arr[nx][ny] = dist + 1

print(*[arr[i][j] for i, j in ans])
