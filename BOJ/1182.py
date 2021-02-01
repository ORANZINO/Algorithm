from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(1, n + 1):
    answer += [sum(c) for c in combinations(nums, i)].count(s)

print(answer)
