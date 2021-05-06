from math import sqrt

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    m = max(r1, r2, dist)
    if m == (sum(r1, r2, dist) - m):
        print(1)
    elif dist == 0 and r1 == r2:
        print(-1)
    elif m > (sum(r1, r2, dist) - m):
        print(0)
    else:
        print(2)
        