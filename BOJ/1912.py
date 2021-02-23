n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i - 1] + arr[i])

print(max(dp))
