a, b = map(int, input().split())
while a != 0 or b != 0:
    print(a + b)
    a, b = map(int, input().split())

"""
a, b가 모두 0이 될 때까지 a + b를 출력 
"""