import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    # 띄어쓰기로 각 어절 구분 후 뒤집어서 다시 붙여주기!
    print(' '.join(map(lambda x: ''.join(reversed(list(x))), input().split())))
