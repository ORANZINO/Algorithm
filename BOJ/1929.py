from math import sqrt

def find_prime(x, y):
    result = [i in range(x, y + 1) for i in range(y + 1)]
    result[1] = False
    for i in range(x, y + 1):
        for j in range(2, int(sqrt(i)) + 1):
            if (i % j) == 0:
                result[i] = False
                break
    for i in range(x, y + 1):
        if result[i]: print(i)


m, n = map(int, input().split())
find_prime(m, n)