from itertools import combinations

n, m = map(int,input().split())
for c in combinations(map(str, range(1, n + 1)), m):
    print(' '.join(c))
