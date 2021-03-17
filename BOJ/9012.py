import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().strip())
    temp = 0
    for i in s:
        if i == '(':
            temp += 1
        elif i == ')':
            temp -= 1
        if temp < 0:
            print('NO')
            break
    if temp > 0:
        print('NO')
    elif temp == 0:
        print('YES')
