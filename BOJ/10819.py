from itertools import permutations

n = int(input())
array = list(map(int, input().split()))

print(max(sum(abs(p[i] - p[i + 1]) for i in range(n - 1)) for p in permutations(array, n)))
