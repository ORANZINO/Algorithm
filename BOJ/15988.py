import sys
input = sys.stdin.readline

t = int(input())
arr = [0] * 1000001
arr[1], arr[2], arr[3] = 1, 2, 4
done = 3
for _ in range(t):
    n = int(input())
    if n > done:
        for i in range(done + 1, n + 1):
            arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000000009
        done = n
    print(arr[n])
