from collections import deque
from copy import deepcopy

r = c = 0


def solve(board, x1, y1, x2, y2):
    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if not any(0 <= x1 + a < r and 0 <= y1 + b < c and board[x1 + a][y1 + b] for a, b in steps):
        return False, 0
    if x1 == x2 and y1 == y2: return True, 1

    win = False
    min_dist, max_dist = int(1e9), 0
    for step in steps:
        nx, ny = x1 + step[0], y1 + step[1]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny]:
            board[x1][y1] = 0
            result = solve(board, x2, y2, nx, ny)
            board[x1][y1] = 1

            if not result[0]:
                win = True
                min_dist = min(min_dist, result[1])
            elif not win:
                max_dist = max(max_dist, result[1])

    dist = min_dist if win else max_dist
    return win, dist + 1


def solution(board, aloc, bloc):
    global r, c
    r, c = len(board), len(board[0])

    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


