n, k = map(int, input().split())

dp = [1] * (n + 1)
k -= 1

while k:
    next_dp = [1] * (n + 1)
    for i in range(1, n + 1):
        next_dp[i] = sum(dp[:i + 1])
    dp = next_dp[:]
    k -= 1

print(dp[-1] % 1000000000)
