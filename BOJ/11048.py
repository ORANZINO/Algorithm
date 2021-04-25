n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# 제일 윗 줄 채우기
for i in range(m):
    dp[0][i] = sum(arr[0][:i+1])
# 제일 왼쪽 줄 채우기
for i in range(1, n):
    dp[i][0] = sum(arr[j][0] for j in range(i + 1))
# 그 외의 칸들 왼쪽 칸과 위쪽 칸 비교 후 더 큰 값 + 해당 칸의 값 할당
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

print(dp[n - 1][m - 1])
