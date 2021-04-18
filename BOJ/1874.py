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

"""
숫자가 주어지고 지금의 포인터가 해당 숫자보다 작으면 해당 숫자만큼 push하고 나서
해당 숫자를 pop한다. 그렇지 않을 경우, 지금 당장 포인터가 가리키는 것이 해당 숫자가 아니라면
불가능한 배열이므로 NO를 출력한 후에 exit한다.
"""
