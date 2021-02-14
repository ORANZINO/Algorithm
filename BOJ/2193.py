from copy import deepcopy

n = int(input())
arr = [0, 1]

for _ in range(n - 1):
    next_arr = [0, 0]
    next_arr[0], next_arr[1] = sum(arr), arr[0]
    arr = deepcopy(next_arr)

print(sum(arr))
