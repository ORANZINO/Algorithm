n = int(input())
arr = list(map(int, input().split()))
dp = [[a, a, a] for a in arr]

if n != 1:
    dp[1][0] = max(dp[1][0], dp[0][0] + arr[1])

for i in range(2, n):
    # plain - without skipping
    dp[i][0] = max(dp[i][0], dp[i - 1][0] + arr[i])
    # skip
    dp[i][1] = max(dp[i][1], dp[i - 2][0] + arr[i], dp[i - 1][1] + arr[i])

print(max(map(max, dp)))
