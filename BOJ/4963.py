import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)

def dfs(v):
    y, x = v
    visited[y][x] = True
    for step in steps:
        nx, ny = x + step[0], y + step[1]
        if 0 <= nx < w and 0 <= ny < h:
            if not visited[ny][nx] and graph[ny][nx]:
                dfs((ny, nx))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    count = 0
    visited = [[False] * w for _ in range(h)]
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]:
                count += 1
                dfs((i, j))
    print(str(count) + '\n')
