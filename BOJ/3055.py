from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
forest = [list(input().strip()) for _ in range(r)]
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0
flag = True
q = deque()

for i in range(r):
    for j in range(c):
        if forest[i][j] == '*':
            q.append(('*', i, j))

for i in range(r):
    for j in range(c):
        if forest[i][j] == 'S':
            forest[i][j] = 0
            q.append((0, i, j))

while q and flag:
    what, y, x = q.popleft()
    for step in steps:
        n_x, n_y = x + step[0], y + step[1]
        if 0 <= n_x < c and 0 <= n_y < r:
            if what == '*':
                if forest[n_y][n_x] not in ['*', 'X', 'D']:
                    forest[n_y][n_x] = '*'
                    q.append(('*', n_y, n_x))
            else:
                if forest[n_y][n_x] == '.':
                    forest[n_y][n_x] = what + 1
                    q.append((what + 1, n_y, n_x))
                elif forest[n_y][n_x] == 'D':
                    answer = what + 1
                    flag = False
                    break

print("KAKTUS" if flag else str(answer))
