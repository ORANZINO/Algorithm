import sys
input = sys.stdin.readline


def check(i, j):
    steps = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]]
    result = 1
    for step in steps:
        count = 1
        for k in range(2):
            x, y = i, j
            while (0 <= x + step[k][0] < n) and (0 <= y + step[k][1] < n) and (arr[x][y] == arr[x + step[k][0]][y + step[k][1]]):
                x += step[k][0]
                y += step[k][1]
                count += 1
        result = max(result, count)
    return result


n = int(input())
arr = [list(input().strip()) for _ in range(n)]

ans = 1

for i in range(n):
    for j in range(n):
        if i < (n - 1):
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            ans = max(ans, check(i, j), check(i + 1, j))
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
        if j < (n - 1):
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            ans = max(ans, check(i, j), check(i, j + 1))
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
print(ans)
