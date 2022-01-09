x = int(input())
i = 1
while x > i:
    x -= i
    i += 1
r = x % (i + 1)
answer = f'{r}/{i + 1 - r}' if i % 2 == 0 else f'{i + 1 - r}/{r}'
print(answer)



"""
규칙에 맞는 분수를 리턴할 수 있게 한다.
"""