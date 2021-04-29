def count_div(target, n):
    count = 0
    temp = target
    while temp != 0:
        temp //= n
        count += temp
    return count

n, m = map(int, input().split())
print(min((count_div(n, 2) - count_div(m, 2) - count_div(n - m, 2)), (count_div(n, 5) - count_div(m, 5) - count_div(n - m, 5))))

