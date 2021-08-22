import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)


"""
입력받은 수들을 더해서 출력한다.
속도를 위해 sys.stdin.readline 함수를 사용했다
"""