n = int(input())
arr = list(map(int, input().split()))
dp = [[1, i] for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i][0] < (dp[j][0] + 1):
            dp[i] = [dp[j][0] + 1, j]

temp = dp.index(max(dp))
route = [temp]

while dp[temp][1] != temp:
    route.insert(0, dp[temp][1])
    temp = dp[temp][1]

print(dp[route[-1]][0])
print(*[arr[r] for r in route], sep=' ')
