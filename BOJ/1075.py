n = int(input()[:-2] + '00')
f = int(input())
for _ in range(100):
    if n % f == 0:
        print(str(n)[-2:])
        break
    n += 1

"""
마지막 2자리 수는 항상 00으로 설정해두고
1씩 올리다가 나누어 떨어질 때 출력하는 방식
"""