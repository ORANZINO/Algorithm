def solution(board, skill):
    n, m = len(board), len(board[0])
    sum_matrix = [[0] * m for _ in range(n)]
    for t, r1, c1, r2, c2, degree in skill:
        t = -1 if t == 1 else 1
        sum_matrix[r1][c1] += t * degree
        if r2 < (n - 1):
            sum_matrix[r2 + 1][c1] -= t * degree
        if c2 < (m - 1):
            sum_matrix[r1][c2 + 1] -= t * degree
        if r2 < (n - 1) and c2 < (m - 1):
            sum_matrix[r2 + 1][c2 + 1] += t * degree
    for j in range(m):
        for i in range(1, n):
            sum_matrix[i][j] += sum_matrix[i - 1][j]
    answer = 0
    for i in range(n):
        for j in range(m):
            if j > 0:
                sum_matrix[i][j] += sum_matrix[i][j - 1]
            if sum_matrix[i][j] + board[i][j] > 0:
                answer += 1
    return answer