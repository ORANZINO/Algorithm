n = int(input())
arr = list(map(int, input().split()))
y = sum(map(lambda x: (x // 30 + 1) * 10, arr))
m = sum(map(lambda x: (x // 60 + 1) * 15, arr))

if m < y:
    print(f'M {m}')
elif m > y:
    print(f'Y {y}')
else:
    print(f'Y M {y}')


"""
map을 써서 주어진 조건을 적용해주고 조건에 맞게 답을 출력해준다
"""