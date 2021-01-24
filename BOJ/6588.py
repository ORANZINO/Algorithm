from math import sqrt

r = 1000000
array = [True] * (r + 1)
for i in range(4, r + 1, 2):
    array[i] = False
for i in range(3, int(sqrt(r)) + 1, 2):
    if array[i]:
        j = i
        while i * j <= r:
            array[i * j] = False
            j += 2
while True:
    n = int(input())
    if n == 0:
        break
    flag = False

    for i in range(3, n // 2 + 1, 2):
        if array[i] and array[n - i]:
            print(f'{n} = {i} + {n - i}')
            flag = True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")
