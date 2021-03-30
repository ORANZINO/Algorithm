n, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
ans = [0 for i in range(k + 1)]
ans[0] = 1

for i in arr:
    j = i
    while j <= k:
        ans[j] += ans[j - i]
        j += 1

print(ans[k])
