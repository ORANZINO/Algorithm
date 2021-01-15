from itertools import combinations
from bisect import bisect_right

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cases = [sum(k) for k in combinations(cards, 3)]
cases.sort()
idx = bisect_right(cases, m)

print(cases[idx - 1])