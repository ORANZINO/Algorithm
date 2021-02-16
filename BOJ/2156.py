import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = [0 for _ in range(n)]
for _ in range(n):
    arr.append(int(input()))

ans[0] = arr[0]
if n > 1:
    ans[1] = arr[0] + arr[1]
if n > 2:
    ans[2] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])

for i in range(3, n):
    ans[i] = max(ans[i - 1], ans[i - 2] + arr[i], ans[i - 3] + arr[i - 1] + arr[i])

print(ans[n - 1])
