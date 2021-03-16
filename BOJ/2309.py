from itertools import combinations
import sys
input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]

for c in combinations(arr, 7):
    if sum(c) == 100:
        print(*sorted(c), sep='\n')
        break

