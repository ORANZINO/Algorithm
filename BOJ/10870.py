n = int(input())

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

for i in range(18, n + 1):
    arr.append(arr[-1] + arr[-2])

print(arr[n])
