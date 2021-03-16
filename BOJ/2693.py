import sys
input = sys.stdin.readline

t = int(input())
print(*[sorted(map(int, input().split()))[-3] for _ in range(t)], sep='\n')
