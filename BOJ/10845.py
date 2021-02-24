import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    temp = input().strip().split()

    if temp[0] == 'push':
        arr.append(temp[1])
    elif temp[0] == 'pop':
        print(arr.pop(0) if arr else -1)
    elif temp[0] == 'size':
        print(len(arr))
    elif temp[0] == 'empty':
        print(1 if not arr else 0)
    elif temp[0] == 'front':
        print(arr[0] if arr else -1)
    elif temp[0] == 'back':
        print(arr[-1] if arr else -1)
