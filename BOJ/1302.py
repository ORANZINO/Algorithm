from collections import Counter

n = int(input())
counter = dict(Counter(input() for _ in range(n)))
print(sorted([key for key in counter.keys() if counter[key] == max(counter.values())])[0])
