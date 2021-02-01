from itertools import product

n, m = map(int, input().split())
for p in sorted(set(product(map(int, input().split()), repeat=m))):
    print(' '.join(map(str, p)))
