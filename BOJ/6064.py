from math import gcd
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    k = x
    y = 0 if n == y else y
    end = (m * n) // gcd(m, n)
    while k <= end:
        if k % n == y:
            break
        k += m
    print(-1 if k > end else k)
