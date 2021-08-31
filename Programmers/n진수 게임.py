def convert(x, n):
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if x < n:
        return arr[x]
    else:
        return convert(x // n, n) + convert(x % n, n)


def solution(n, t, m, p):
    arr = [(p - 1) + i * m for i in range(t)]
    i = 0
    s = ''
    while len(s) <= max(arr):
        s += convert(i, n)
        i += 1
    return ''.join(s[i] for i in arr)

