import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1002

for i in range(n):
    dp[arr[i]] = max(dp[arr[i] + 1:]) + 1

print(max(dp))
