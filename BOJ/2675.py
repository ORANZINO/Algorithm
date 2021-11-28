t = int(input())
for _ in range(t):
    r, s = input().split()
    print(''.join(i * int(r) for i in s))


"""
입력받은 문자열의 캐릭터마다 r배하여 출력
"""