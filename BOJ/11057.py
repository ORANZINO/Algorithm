from copy import deepcopy

n = int(input())
arr = [1] * 10

for _ in range(n - 1):
    next_arr = [0] * 10
    for i in range(10):
        for j in range(i, 10):
            next_arr[j] += arr[i] % 10007
    arr = deepcopy(next_arr)

print(sum(arr) % 10007)
