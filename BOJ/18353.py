n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(i, -1, -1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
