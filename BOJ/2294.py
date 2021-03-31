import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = [100001 for i in range(k + 1)]
ans[0] = 0

for i in arr:
    for j in range(i, k + 1):
        ans[j] = min(ans[j], ans[j - i] + 1)

print(-1 if ans[k] == 100001 else ans[k])
