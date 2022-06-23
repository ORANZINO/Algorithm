nums = [
    int('1110111', 2),
    int('0010010', 2),
    int('1011101', 2),
    int('1011011', 2),
    int('0111010', 2),
    int('1101011', 2),
    int('1101111', 2),
    int('1010010', 2),
    int('1111111', 2),
    int('1111011', 2),
        ]
def backtrack(i, N, K, P, X):
    if i == K or P == 0:
        temp = int(''.join(X))
        if 0 < temp <= N:
            global answer
            print('temp: ', temp)
            answer.add(temp)
        return
    global nums
    now = nums[int(X[i])]
    for j in range(10):
        if now == nums[j]:
            backtrack(i + 1, N, K, P, X.copy())
        else:
            need = bin(now ^ nums[j]).count('1')
            if need <= P:
                save = X[i]
                X[i] = str(j)
                backtrack(i + 1, N, K, P - need, X.copy())
                X[i] = save



N, K, P, X = map(int, input().split())
answer = set()
X = list(str(X).zfill(K))
backtrack(0, N, K, P, X)
answer.remove(int(''.join(X)))
print(len(answer))
