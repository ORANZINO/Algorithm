from itertools import combinations_with_replacement

n, m = map(int,input().split())
for c in combinations_with_replacement(map(str, range(1, n + 1)), m):
    print(' '.join(c))