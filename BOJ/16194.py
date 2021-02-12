n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)

for i in range(2, n + 1):
    for j in range(i - 1, 0, -1):
        p[i] = min(p[i], p[i - j] + p[j])

print(p[n])
