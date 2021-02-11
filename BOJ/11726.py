n = int(input())
array = [0] * (n + 2)
array[1], array[2] = 1, 2

for i in range(3, n + 1):
    array[i] = array[i - 1] + array[i - 2]

print(array[n] % 10007)

