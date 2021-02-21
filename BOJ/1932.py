import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = [[0] * (i + 1) for i in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][0] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][i - 1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]

print(max(dp[-1]))
