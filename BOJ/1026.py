n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

print(sum(a[i] * b[i] for i in range(len(a))))

"""
a에서 최소인 수를 b에서 최대인 수와 곱하도록 정렬하여 합한다.
"""