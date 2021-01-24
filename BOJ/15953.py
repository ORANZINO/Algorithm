first = [500] + [300] * 2 + [200] * 3 + [50] * 4 + [30] * 5 + [10] * 6
second = [512] + [256] *2 + [128] * 4 + [64] * 8 + [32] * 16

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    answer = 0
    if 0 <= a < len(first):
        answer += first[a]
    if 0 <= b < len(second):
        answer += second[b]
    print(answer * 10000)
