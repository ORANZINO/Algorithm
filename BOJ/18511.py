from itertools import product

n, k_num = map(int, input().split())
l = len(str(n))
k = list(input().split())

candidates = [int(''.join(p)) for p in product(k, repeat=l)]
ans = [c for c in candidates if c <= n]
print(max(ans) if ans else max(k)*(l - 1))
