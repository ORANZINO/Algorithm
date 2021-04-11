import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
our = []
enemy = []
steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            temp = 1
            while q:
                x, y = q.popleft()
                for step in steps:
                    next_x, next_y = x + step[0], y + step[1]
                    if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y] and arr[next_x][next_y] == arr[x][y]:
                        visited[next_x][next_y] = True
                        temp += 1
                        q.append((next_x, next_y))
            our.append(temp ** 2) if arr[i][j] == 'W' else enemy.append(temp ** 2)

print(sum(our), sum(enemy))
