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
# 음식물의 위치 이중 Array에 표시
for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = True
# 방문하지 않은 음식물을 만날 때마다 DFS를 사용해서 총 몇 개가 붙어있는지 확인
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            now = 0
            visited[i][j] = True
            dfs(i, j)
            ans = max(ans, now)
# 가장 큰 덩어리의 크기를 출력
print(ans)
