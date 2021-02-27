n = int(input())
arr = [[0, 0] for _ in range(n + 1)]
arr[1] = [1, 2]
for i in range(2, n + 1):
    arr[i] = [sum(arr[i - 1]) % 9901, (arr[i - 1][0] * 2 + arr[i - 1][1]) % 9901]
print(sum(arr[n]) % 9901)
