from math import sqrt


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if (x % i) == 0:
            return False
    return True


m = int(input())
n = int(input())
arr = [i for i in range(m, n + 1) if is_prime(i)]
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
