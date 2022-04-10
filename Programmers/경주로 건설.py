from collections import deque

def solution(board):
    N, INF = len(board), int(1e6)
    cost = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    cost[0][0] = [0, 0, 0, 0]
    q = deque()
    if board[0][1] != 1:
        q.append((0, 1, 2))
        cost[0][1][2] = 100
    if board[1][0] != 1:
        q.append((1, 0, 0))
        cost[1][0][0] = 100
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y, direction = q.popleft()
        for i, step in enumerate(steps):
            nx, ny = x + step[0], y + step[1]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = cost[x][y][direction] + 100 if direction == i else cost[x][y][direction] + 600
                if new_cost < cost[nx][ny][i]:
                    q.append((nx, ny, i))
                    cost[nx][ny][i] = new_cost
    return min(cost[-1][-1])

