import sys
input = sys.stdin.readline

arr = []
temp = 0
for _ in range(10):
    a, b = map(int, input().split())
    temp += (b - a)
    arr.append(temp)
print(max(arr))
