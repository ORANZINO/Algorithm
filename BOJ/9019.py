from collections import deque
import sys


def check(x, char):
    global parents
    global q
    global b
    global a
    global temp
    if parents[x][0] == -1:
        parents[x][0] = temp
        parents[x][1] = char
        q.append(x)
    if b == x:
        answer = ''
        while b != a:
            answer = parents[b][1] + answer
            b = parents[b][0]
        print(answer)
        return True

    return False


input = sys.stdin.readline
t = int(input())

for _ in range(t):
    parents = [[-1, ''] for _ in range(10000)]
    a, b = map(int, input().split())
    q = deque()
    q.append(a)

    while q:
        temp = q.popleft()
        d = temp * 2 % 10000
        if check(d, 'D'):
            break
        s = 9999 if temp == 0 else temp - 1
        if check(s, 'S'):
            break
        l = (temp % 1000) * 10 + (temp // 1000)
        if check(l, 'L'):
            break
        r = (temp % 10) * 1000 + (temp // 10)
        if check(r, 'R'):
            break
