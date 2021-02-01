def backtrack(A, add, subtract, multiply, divide, result):
    if not A:
        global max_val
        global min_val
        max_val = max(max_val, result)
        min_val = min(min_val, result)
    else:
        if add:
            backtrack(A[1:], add - 1, subtract, multiply, divide, result + A[0])
        if subtract:
            backtrack(A[1:], add, subtract - 1, multiply, divide, result - A[0])
        if multiply:
            backtrack(A[1:], add, subtract, multiply - 1, divide, result * A[0])
        if divide:
            if result < 0:
                backtrack(A[1:], add, subtract, multiply, divide - 1, -(-result // A[0]))
            else:
                backtrack(A[1:], add, subtract, multiply, divide - 1, result // A[0])

n = int(input())
A = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

INF = int(1e9)
max_val = -INF
min_val = INF

backtrack(A[1:], add, subtract, multiply, divide, A[0])

print(max_val)
print(min_val)

