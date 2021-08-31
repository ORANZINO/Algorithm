def check(i, j, board):
    steps = [(0, 1), (1, 0), (1, 1)]
    return board[i][j] != '0' and all(board[i][j] == board[i + s[0]][j + s[1]] for s in steps)


def solution(m, n, board):
    steps = [(0, 0), (1, 0), (0, 1), (1, 1)]
    board = [[board[j][i] for j in range(m)] for i in range(n)]
    flag = True
    count = 0
    print(*board, sep='\n')
    while flag:
        flag = False
        erase = [[False] * m for _ in range(n)]
        q = []
        for i in range(n - 1):
            for j in range(m - 1):
                if check(i, j, board):
                    flag = True
                    for step in steps:
                        if not erase[i + step[0]][j + step[1]]:
                            erase[i + step[0]][j + step[1]] = True
                            q.append((i + step[0], j + step[1]))
        q.sort()
        while q:
            x, y = q.pop(0)
            board[x].pop(y)
            board[x].insert(0, '0')
            count += 1

    return count


