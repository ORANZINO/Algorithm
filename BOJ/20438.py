import sys

input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleeping = set(map(int, input().split()))
check = set(map(int, input().split()))
until = [0] * (n + 3)
for i in range(3, n + 3):
    until[i] = until[i - 1] + (i in sleeping or all(i % c != 0 for c in (check - sleeping)))
answer = ""
for _ in range(m):
    s, e = map(int, input().split())
    answer += f'{until[e] - until[s - 1]}\n'
print(answer)

