t = int(input())
arr = [int(input()) for _ in range(t)]
dp = [0] * (max(arr) + 1)
dp[0] = 1
for i in range(1, 4):
    for j in range(i, len(dp)):
        dp[j] += dp[j - i]

for a in arr:
    print(dp[a])
