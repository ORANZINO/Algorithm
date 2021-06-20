n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        if temp >= m:
            if temp == m:
                ans += 1
            break
print(ans)

# 브루트 포스 방식으로 
