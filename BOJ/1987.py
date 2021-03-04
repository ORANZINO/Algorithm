import sys
input = sys.stdin.readline

def dfs(y, x, n):
    global ans
    ans = max(ans, n)
    for step in steps:
        nx, ny = x + step[0], y + step[1]
        if 0 <= nx < c and 0 <= ny < r and not visited[arr[ny][nx]]:
            if not visited[arr[ny][nx]]:
                visited[arr[ny][nx]] = True
                dfs(ny, nx, n + 1)
                visited[arr[ny][nx]] = False


r, c = map(int, input().split())
arr = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [False] * 26
visited[arr[0][0]] = True
ans = 0
dfs(0, 0, 1)
print(ans)
