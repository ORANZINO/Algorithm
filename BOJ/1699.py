from math import sqrt

n = int(input())
sq_num = [i ** 2 for i in range(1, int(sqrt(n) + 1))]
dp = [1 if i in sq_num else i for i in range(n + 1)]
for i in range(2, n + 1):
    for j in range(1, int(sqrt(i)) + 1):
        dp[i] = min(dp[i], 1 + dp[i - j ** 2])
print(dp[n])
