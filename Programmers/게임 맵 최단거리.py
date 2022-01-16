from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0, 1,))
    visited[0][0] = True
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y, dist = q.popleft()
        for step in steps:
            nx, ny = x + step[0], y + step[1]
            if nx == (n - 1) and ny == (m - 1):
                return dist + 1
            elif 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    return -1

