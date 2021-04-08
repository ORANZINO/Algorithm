import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: 가로로 온 수 / 1: 세로로 온 수 / 2: 대각선으로 온 수
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
i = 2
while i < n:
    if arr[0][i]:
        break
    dp[0][0][i] = 1
    i += 1

for i in range(1, n):
    for j in range(2, n):
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][-1][-1] for i in range(3)))
