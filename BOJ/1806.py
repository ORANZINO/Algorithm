
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = n + 1
temp = 0
start = 0
for i in range(n):
    temp += arr[i]
    if temp >= s:
        while temp >= s:
            temp -= arr[start]
            start += 1
        ans = min(ans, i - start + 2)

print(0 if ans > n else ans)
