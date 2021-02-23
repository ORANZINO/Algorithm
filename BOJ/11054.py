n = int(input())
arr = list(map(int, input().split()))

dp = [[1, 1] for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            # 증가 수열
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
            # 감소 수열로 전환
            dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        elif arr[i] < arr[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

print(max(max(dp)[0], max(dp, key=lambda x: x[1])[1]))
