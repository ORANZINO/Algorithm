# 첫 번째 풀이

from itertools import combinations

n = int(input())
arr = [[0] * (n + 1)]
ans = int(1e9)
whole = set(range(1, n + 1))

for i in range(n):
    arr.append([0] + list(map(int, input().split())))

for com in combinations(range(2, n + 1), n // 2 - 1):
    our = set([1]) | set(com)
    enemy = whole - our
    diff = abs(sum(arr[x][y] for x in our for y in our - set([x])) - sum(arr[x][y] for x in enemy for y in enemy - set([x])))
    ans = min(ans, diff)
    if ans == 0: break

print(ans)


# 두 번째 풀이

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
each = [sum(x) + sum(y) for x, y in zip(arr, zip(*arr))]
total = sum(each) // 2

print(min(abs(total - sum(each[e] for e in c)) for c in combinations(range(1, n), n // 2)))
