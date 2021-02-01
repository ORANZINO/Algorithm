from itertools import combinations

n, m = map(int, input().split())

for p in sorted(set(map(tuple, map(sorted, combinations((map(int, input().split())), m))))):
    print(' '.join(map(str, p)))
