def solution(n):
    if n == 2:
        return 3
    dp, acc = [0] * (n // 2 + 1), [0] * (n // 2)
    dp[0], dp[1], acc[0] = 1, 3, 1
    for i in range(2, n // 2 + 1):
        dp[i] = dp[i - 1] * 3 + 2 * acc[i - 2]
        acc[i - 1] = acc[i - 2] + dp[i - 1]
    return dp[-1] % 1000000007

