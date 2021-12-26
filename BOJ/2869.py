from math import ceil

a, b, v = map(int, input().split())
print(ceil((v - a) / (a - b)) + 1)

'''
마지막에는 무조건 a만큼 갔다고 가정하고 나눗셈을 한다.
a만큼 간 것도 1일치이므로 1일을 더해주는 것을 잊지 않도록 한다.
'''