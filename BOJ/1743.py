import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    global now
    now += 1
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for step in steps:
        nx, ny = x + step[0], y + step[1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

n, m, k = map(int, input().split())
arr = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 1
for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = True
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            now = 0
            visited[i][j] = True
            dfs(i, j)
            ans = max(ans, now)

print(ans)
