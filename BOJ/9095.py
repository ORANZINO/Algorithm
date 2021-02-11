# 첫 번째 풀이

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    q = deque()
    answer = 0
    if 1 <= n:
        q.append(1)
    if 2 <= n:
        q.append(2)
    if 3 <= n:
        q.append(3)
    while q:
        temp = q.popleft()
        if temp == n:
            answer += 1
        if temp + 1 <= n:
            q.append(temp + 1)
        if temp + 2 <= n:
            q.append(temp + 2)
        if temp + 3 <= n:
            q.append(temp + 3)
    print(answer)


# 두 번째 풀이
import sys
input = sys.stdin.readline
n_arr = []
arr = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
t = int(input())
for _ in range(t):
    n_arr.append(int(input()))
ans = [arr[n] for n in n_arr]
print(*ans, sep='\n')