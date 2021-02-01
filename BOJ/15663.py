from itertools import permutations

n, m = map(int, input().split())

for p in sorted(set(permutations((map(int, input().split())), m))):
    print(' '.join(map(str, p)))
