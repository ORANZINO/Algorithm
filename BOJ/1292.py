a, b = map(int, input().split())
arr = [i for i in range(1, 47) for _ in range(i)]
print(sum(arr[a - 1:b]))
