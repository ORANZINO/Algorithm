import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    print(' '.join(map(lambda x: ''.join(reversed(list(x))), input().split())))
