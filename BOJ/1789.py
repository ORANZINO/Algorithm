s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)

"""
제일 작은 서로 다른 수들을 더하다가 주어진 수를 넘어설 때 그 수보다 1 작은 수를 취하면 된다. 
"""