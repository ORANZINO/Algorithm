input()
a = set(map(int, input().split()))
input()
b = list(map(int, input().split()))
result = []

for i in b:
    if i in a:
        print('1', end=' ')
    else:
        print('0', end=' ')