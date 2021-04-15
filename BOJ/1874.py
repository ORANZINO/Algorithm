import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ptr = 1
stack = deque()
ans = []
for _ in range(n):
    num = int(input())
    while ptr <= num:
        stack.append(ptr)
        ans.append('+')
        ptr += 1
    if stack[-1] == num:
        ans.append('-')
        stack.pop()
    else:
        print("NO")
        exit()
print(*ans, sep='\n')
