import sys

m = int(input())
s = 0

for _ in range(m):
    op = sys.stdin.readline().strip().split()
    if len(op) == 1:
        if op[0] == 'all':
            s = (1 << 20) - 1
        elif op[0] == 'empty':
            s = 0
        continue
    op, num = op
    num = int(num) - 1
    if op == 'add':
        s = s | (1 << num)
    elif op == 'remove':
        s = s & ~(1 << num)
    elif op == 'check':
        if (1 << num) & s != 0:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if (1 << num) & s != 0:
            s = s & ~(1 << num)
        else:
            s = s | (1 << num)
