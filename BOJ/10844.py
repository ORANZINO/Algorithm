from copy import deepcopy

n = int(input())
arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(n - 1):
    next_arr = [0] * 10
    for i in range(1, 9):
        next_arr[i - 1] += arr[i]
        next_arr[i + 1] += arr[i]
    next_arr[1] += arr[0]
    next_arr[8] += arr[9]
    arr = deepcopy([nxt % int(1e9) for nxt in next_arr])

print(sum(arr) % int(1e9))
