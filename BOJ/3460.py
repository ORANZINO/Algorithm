t = int(input())

for _ in range(t):
    n = list(bin(int(input()))[2:])
    n.reverse()
    print(*[i for i in range(len(n)) if n[i] == '1'])
