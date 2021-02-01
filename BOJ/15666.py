from itertools import combinations_with_replacement

n, m = map(int, input().split())
for c in sorted(set(combinations_with_replacement(sorted(map(int, input().split())), m))):
    print(' '.join(map(str, c)))
