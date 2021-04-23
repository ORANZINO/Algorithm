from math import factorial

n = factorial(int(input()))
temp = 10
ans = 0
while n % temp == 0:
    temp *= 10
    ans += 1
print(ans)
