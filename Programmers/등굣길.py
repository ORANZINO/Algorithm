def solution(m, n, puddles):
    area = [[0] * n for _ in range(m)]
    for x, y in puddles:
        area[x - 1][y - 1] = -1
    area[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                area[i][j] = 0 if area[i][j] == -1 else area[i - 1][j] + area[i][j - 1]
            elif i > 0:
                area[i][j] = 0 if area[i][j] == -1 else area[i - 1][j]
            elif j > 0:
                area[i][j] = 0 if area[i][j] == -1 else area[i][j - 1]
    return area[-1][-1] % 1000000007


