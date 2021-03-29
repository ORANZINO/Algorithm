n, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
ans = [0 for i in range(k + 1)]
ans[0] = 1

for i in arr:
    for j in range(1, k + 1):
        if j >= i:
            ans[j] += ans[j - i]


print(ans[k])
