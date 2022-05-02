import heapq


def tail(x, y, pos):
    return (x - 1, y) if pos else (x, y - 1)


def solution(board):
    INF, n = int(1e9), len(board)
    distance = [[[INF, INF] for _ in range(n)] for _ in range(n)]
    distance[0][1][0] = 0
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = []
    heapq.heappush(q, (0, 0, 1, 0))

    while q:
        dist, x, y, pos = heapq.heappop(q)
        npos = (pos + 1) % 2
        tx, ty = tail(x, y, pos)
        for step in steps:
            nx, ny = x + step[0], y + step[1]
            tnx, tny = tail(nx, ny, pos)
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and 0 <= tnx < n and 0 <= tny < n and board[tnx][tny] != 1:
                if distance[nx][ny][pos] > (dist + 1):
                    heapq.heappush(q, (dist + 1, nx, ny, pos))
                    distance[nx][ny][pos] = dist + 1
                if step[pos] != 0:
                    if step[pos] == -1:
                        nx, ny, tnx, tny = x, y, tx, ty
                    if distance[nx][ny][npos] > (dist + 1):
                        heapq.heappush(q, (dist + 1, nx, ny, npos))
                        distance[nx][ny][pos] = dist + 1
                    if distance[tnx][tny][npos] > (dist + 1):
                        heapq.heappush(q, (dist + 1, tnx, tny, npos))
                        distance[tnx][tny][npos] = dist + 1
        if min(distance[-1][-1]) != INF:
            return min(distance[-1][-1])

