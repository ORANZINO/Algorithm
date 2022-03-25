from collections import deque

n = int(input())
k = int(input())
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1
l = int(input())
turns = [input().split() for _ in range(l)]
turn_idx = 0
board[1][1] = 2
now = [1, 1, 0, 0] # x, y, direction, time
q = deque()
q.append((1, 1))
while True:
    x, y, d_idx, time = now
    nx, ny = x + directions[d_idx][0], y + directions[d_idx][1]
    if 0 < nx <= n and 0 < ny <= n and board[nx][ny] != 2:
        if board[nx][ny] != 1:
            px, py = q.popleft()
            board[px][py] = 0
        board[nx][ny] = 2
        x, y = nx, ny
        q.append((x, y))
        time += 1
        if turn_idx < len(turns) and int(turns[turn_idx][0]) == time:
            if turns[turn_idx][1] == 'L':
                d_idx = (d_idx - 1) % 4
            else:
                d_idx = (d_idx + 1) % 4
            turn_idx += 1
        now = [x, y, d_idx, time]
    else:
        now[-1] += 1
        break
print(now[-1])