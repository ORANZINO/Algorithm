t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    ans = [[0] * n for _ in range(2)]
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        if i == 0:
            ans[0][0] = arr[0][0]
            ans[1][0] = arr[1][0]
        elif i == 1:
            ans[0][1] = arr[1][0] + arr[0][1]
            ans[1][1] = arr[0][0] + arr[1][1]
        else:
            ans[0][i] = arr[0][i] + max(ans[1][i - 1], ans[1][i - 2])
            ans[1][i] = arr[1][i] + max(ans[0][i - 1], ans[0][i - 2])
    print(max(ans[0][n - 1], ans[1][n - 1]))
