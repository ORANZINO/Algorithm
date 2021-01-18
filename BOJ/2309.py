from itertools import combinations
arr = []
for _ in range(9):
    arr.append(int(input()))

cases = list(combinations(arr, 7))

for case in cases:
    if sum(case) == 100:
        temp = list(case)
        temp.sort()
        for t in temp:
            print(t)
        break
