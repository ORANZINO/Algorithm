import sys
input = sys.stdin.readline

t = int(input())
n_arr = []
arr = [[0, 0, 0] for _ in range(100001)]
arr[1], arr[2], arr[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]

for _ in range(t):
    n_arr.append(int(input()))

max_val = max(n_arr)

for i in range(4, max_val + 1):
    arr[i][0] = (arr[i - 1][1] + arr[i - 1][2]) % 1000000009
    arr[i][1] = (arr[i - 2][0] + arr[i - 2][2]) % 1000000009
    arr[i][2] = (arr[i - 3][0] + arr[i - 3][1]) % 1000000009

ans = [sum(arr[n]) % 1000000009 for n in n_arr]

print(*ans, sep='\n')
