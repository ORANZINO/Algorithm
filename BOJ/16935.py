N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ops = list(map(int, input().split()))

for key in ops:
    if key == 1:
        for i in range(N // 2):
            A[i], A[-i - 1] = A[-i - 1], A[i]
    elif key == 2:
        for i in range(N):
            for j in range(M // 2):
                A[i][j], A[i][-j - 1] = A[i][-j - 1], A[i][j]
    elif key == 3:
        result = []
        for i in range(M):
            temp = []
            for j in range(N - 1, -1, -1):
                temp.append(A[j][i])
            result.append(temp)
        A = result
        N, M = M, N
    elif key == 4:
        result = []
        for i in range(M - 1, -1, -1):
            temp = []
            for j in range(N):
                temp.append(A[j][i])
            result.append(temp)
        A = result
        N, M = M, N
    elif key == 5:
        for i in range(N // 2):
            A[i], A[i + N // 2] = A[i + N // 2], A[i]
        for i in range(N // 2, N):
            for j in range(M // 2):
                A[i][j], A[i - N // 2][j + M // 2] = A[i - N // 2][j + M // 2], A[i][j]
    elif key == 6:
        for i in range(N // 2):
            A[i], A[i + N // 2] = A[i + N // 2], A[i]
        for i in range(N // 2):
            for j in range(M // 2):
                A[i][j], A[i + N // 2][j + M // 2] = A[i + N // 2][j + M // 2], A[i][j]

for arr in A:
    print(*arr, sep=' ')