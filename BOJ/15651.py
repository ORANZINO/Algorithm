from itertools import product

n, m = map(int,input().split())
for c in product(map(str, range(1, n + 1)), repeat=m):
    print(' '.join(c))

